import Foundation
import PDFKit
import AppKit

guard CommandLine.arguments.count == 3 else {
    print("Usage: swift script.swift <input_pdf_path> <output_directory>")
    exit(1)
}

let inputPath = CommandLine.arguments[1]
let outputDir = CommandLine.arguments[2]

let pdfURL = URL(fileURLWithPath: inputPath)
guard let document = PDFDocument(url: pdfURL) else {
    print("Error: Could not load PDF at \(inputPath)")
    exit(1)
}

// Create output directory if it doesn't exist
let fileManager = FileManager.default
try? fileManager.createDirectory(atPath: outputDir, withIntermediateDirectories: true, attributes: nil)

print("Processing \(document.pageCount) pages...")

for i in 0..<document.pageCount {
    autoreleasepool {
        guard let page = document.page(at: i) else { return }
        let pageRect = page.bounds(for: .mediaBox)
        let imgSize = pageRect.size
        
        let image = page.thumbnail(of: imgSize, for: .mediaBox)
        
        if let tiffData = image.tiffRepresentation,
           let bitmap = NSBitmapImageRep(data: tiffData),
           let pngData = bitmap.representation(using: .png, properties: [:]) {
            
            let filename = "page_\(i + 1).png"
            let outputURL = URL(fileURLWithPath: outputDir).appendingPathComponent(filename)
            
            do {
                try pngData.write(to: outputURL)
                print("Saved \(filename)")
            } catch {
                print("Error saving \(filename): \(error)")
            }
        }
    }
}

# Deployment Guide - AppKuitansiBOS

This guide explains how to build and deploy AppKuitansiBOS across different platforms using GitHub Actions.

## Automated Builds

The application is automatically built for Windows, Linux, and macOS using GitHub Actions whenever:
- Code is pushed to `main` or `develop` branches
- A new version tag is created (e.g., `v1.0.0`)
- Pull requests are made to `main`

## Platform-Specific Features

### Windows Build
- **Portable Ghostscript**: Includes a portable version of Ghostscript for PDF processing
- **Portable Poppler**: Includes Poppler utilities for PDF operations
- **No Installation Required**: All dependencies are bundled
- **Output**: `AppKuitansiBOS-Windows.zip`

### Linux Build
- **System Dependencies**: Requires system-installed Ghostscript and Poppler
- **Qt6 Support**: Built with Qt6 libraries
- **Output**: `AppKuitansiBOS-Linux.tar.gz`

### macOS Build
- **Homebrew Dependencies**: Uses Homebrew-installed dependencies
- **App Bundle**: Creates a proper macOS application bundle
- **Output**: `AppKuitansiBOS-macOS.tar.gz`

## Manual Build Instructions

### Prerequisites
```bash
# Install Python 3.11+
python --version

# Install dependencies
pip install -r requirements.txt
pip install pyinstaller
```

### Windows Manual Build
```bash
# Install portable dependencies (manual)
# Download Ghostscript from: https://www.ghostscript.com/download/gsdnld.html
# Download Poppler from: https://github.com/oschwartz10612/poppler-windows

# Build with PyInstaller
pyinstaller build.spec

# Or use the simple command:
pyinstaller --onefile --windowed --name="AppKuitansiBOS" main.py
```

### Linux Manual Build
```bash
# Install system dependencies
sudo apt-get install qt6-base-dev ghostscript poppler-utils

# Build
pyinstaller build.spec
```

### macOS Manual Build
```bash
# Install dependencies
brew install ghostscript poppler qt6

# Build
pyinstaller build.spec
```

## GitHub Actions Workflow

The build process includes:

1. **Environment Setup**
   - Python 3.11 installation
   - Platform-specific dependency installation
   - Requirements caching for faster builds

2. **Windows-Specific Steps**
   - Downloads portable Ghostscript and Poppler
   - Bundles them with the application
   - Creates a self-contained executable

3. **Build Process**
   - Uses PyInstaller with optimized settings
   - Includes all necessary data files
   - Excludes unnecessary packages to reduce size

4. **Packaging**
   - Creates platform-specific archives
   - Uploads artifacts for each platform
   - Automatic release creation for tagged versions

## Customizing Builds

### Adding Dependencies
Update `requirements.txt` with new Python packages:
```txt
new-package>=1.0.0
```

### Modifying Build Settings
Edit `build.spec` to:
- Add/remove data files
- Include/exclude modules
- Change build options

### Platform-Specific Modifications
Edit `.github/workflows/build.yml` to:
- Add system dependencies
- Modify packaging steps
- Change build flags

## Troubleshooting

### Common Issues

1. **Missing Dependencies**
   - Ensure all required packages are in `requirements.txt`
   - Check system dependencies are properly installed

2. **Ghostscript Issues (Windows)**
   - Verify portable Ghostscript is included in build
   - Check PATH configuration in startup script

3. **Large Build Size**
   - Review `excludes` in `build.spec`
   - Remove unnecessary data files

4. **Cross-Platform Compatibility**
   - Test builds on target platforms
   - Verify file paths use correct separators

### Debug Builds
For debugging, create a console version:
```bash
pyinstaller --onefile --console --name="AppKuitansiBOS-Debug" main.py
```

## Release Process

1. **Create a Tag**
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```

2. **Automatic Build**
   - GitHub Actions builds all platforms
   - Creates release with artifacts

3. **Manual Release**
   - Download artifacts from GitHub Actions
   - Test on target platforms
   - Create release manually if needed

## File Structure

```
AppKuitansiBOS/
├── .github/workflows/build.yml    # GitHub Actions workflow
├── build.spec                     # PyInstaller specification
├── requirements.txt               # Python dependencies
├── scripts/setup_windows.py       # Windows setup script
├── main.py                        # Application entry point
├── ui/                            # UI files
├── modules/                       # Application modules
├── data/                          # Database files
└── contoh/                        # Sample files
```

## Distribution

### Windows
- Extract `AppKuitansiBOS-Windows.zip`
- Run `AppKuitansiBOS.exe`
- No additional installation required

### Linux
- Extract `AppKuitansiBOS-Linux.tar.gz`
- Install system dependencies:
  ```bash
  sudo apt-get install ghostscript poppler-utils
  ```
- Run `./run.sh` or `./AppKuitansiBOS`

### macOS
- Extract `AppKuitansiBOS-macOS.tar.gz`
- Install dependencies:
  ```bash
  brew install ghostscript poppler
  ```
- Run `./AppKuitansiBOS` or create an app bundle

## Security Considerations

- Portable dependencies are downloaded from official sources
- All builds are created in isolated GitHub Actions environments
- No sensitive information is included in builds
- Releases are signed where possible (platform-dependent)

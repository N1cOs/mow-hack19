module.exports = {
  lintOnSave: false,
  devServer: {
    proxy: {
      'bws': {
        target: 'http://194.58.90.165/',
        changeOrigin: true,
        secure: false
      }
    }
  }
}
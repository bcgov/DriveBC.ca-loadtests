const maptiler = {
  version: 8,
  sources: {
    maptiler: {
      type: 'raster',
      tiles: ['https://api.maptiler.com/tiles/satellite/{z}/{x}/{y}.png?key=AITV1LUU17CaN7lfvmfi'],
      tileSize: 256,
      maxzoom: 19,
    },
  },
  layers: [
    {
      id: 'mt',
      type: 'raster',
      source: 'maptiler ',
    },
  ],
};

export default maptiler;
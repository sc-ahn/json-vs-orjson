// script.js

// 비동기 함수를 사용하여 JSON 파일 읽기
async function loadJSON(filePath) {
  try {
      // JSON 파일의 경로 설정
      const response = await fetch(filePath);

      // fetch가 완료되면 JSON 데이터 파싱
      const jsonData = await response.json();

      return jsonData;

  } catch (error) {
      console.error('Error reading JSON file:', error);
  }
}


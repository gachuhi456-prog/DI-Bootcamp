

const express = require('express');
const router = express.Router();

const triviaQuestions = [
  { question: "What is the capital of France?", answer: "Paris" },
  { question: "Which planet is known as the Red Planet?", answer: "Mars" },
  { question: "What is the largest mammal in the world?", answer: "Blue whale" },
];

// Simple in-memory state
let gameState = {
  currentIndex: 0,
  score: 0
};

// GET /quiz - Start or show current question
router.get('/', (req, res) => {
  if (gameState.currentIndex >= triviaQuestions.length) {
    return res.redirect('/quiz/score');
  }

  const currentQuestion = triviaQuestions[gameState.currentIndex].question;
  res.send({
    message: "Trivia Quiz Started!",
    questionNumber: gameState.currentIndex + 1,
    question: currentQuestion
  });
});

// POST /quiz - Submit an answer
router.post('/', (req, res) => {
  const userAnswer = req.body.answer;
  const correctAnswer = triviaQuestions[gameState.currentIndex].answer;

  if (!userAnswer) {
    return res.status(400).send({ error: "Please provide an answer in the request body." });
  }

  let feedback = "";
  if (userAnswer.toLowerCase() === correctAnswer.toLowerCase()) {
    gameState.score++;
    feedback = "Correct!";
  } else {
    feedback = `Wrong! The correct answer was ${correctAnswer}.`;
  }

  gameState.currentIndex++;

  res.send({
    feedback: feedback,
    nextStep: gameState.currentIndex < triviaQuestions.length ? "Proceed to GET /quiz for the next question" : "Quiz finished! GET /quiz/score to see results"
  });
});

// GET /quiz/score - Show final result
router.get('/score', (req, res) => {
  res.send({
    finalScore: gameState.score,
    totalQuestions: triviaQuestions.length,
    message: "Thanks for playing!"
  });
});

module.exports = router;

const express = require('express');
const quizRouter = require('./quizRouter');

const app = express();
const PORT = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// Mount the router
app.use('/quiz', quizRouter);

app.listen(PORT, () => {
  console.log(`Trivia game running at http://localhost:${PORT}`);
});


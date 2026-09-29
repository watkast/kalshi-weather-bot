# Gold & Silver Fair-Value Bot

*Updated Mon Sep 28, 10:20 PM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

⏳ **Too early.** 24 of 30 settled trades needed before judging.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 26 | 24 | 11 (46%) | 37¢ | 45% | $16.31 | +17% |
| Silver | 13 | 12 | 4 (33%) | 32¢ | 39% | $0.19 | +0% |
| Gold | 13 | 12 | 7 (58%) | 43¢ | 51% | $16.12 | +30% |

*Earlier half $4.50 / later half $11.81.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 24 | 9 (38%) | -$12.00 | -12% |
| 4¢+ ← live bot | 23 | 9 (39%) | $5.21 | +6% |
| 6¢+ | 23 | 8 (35%) | $7.53 | +10% |
| 8¢+ | 22 | 8 (36%) | $19.99 | +33% |
| 10¢+ | 20 | 5 (25%) | $3.30 | +7% |
| 15¢+ | 9 | 4 (44%) | $20.38 | +104% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 597 | -2.1% |
| Hyperliquid price vs Kalshi's target | 597 | -9.5% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 10:16:38 PM | Silver | DOWN | 13.4 min | 40¢ | 51% | 9¢ | Open | — |
| 9/28 10:16:04 PM | Gold | UP | 13.9 min | 37¢ | 43% | 4¢ | Open | — |
| 9/28 10:01:37 PM | Silver | UP | 13.4 min | 32¢ | 39% | 5¢ | ❌ Lost | -$3.36 |
| 9/28 10:01:05 PM | Gold | UP | 13.9 min | 36¢ | 43% | 5¢ | ❌ Lost | -$3.77 |
| 9/28 9:51:10 PM | Silver | UP | 8.8 min | 31¢ | 41% | 9¢ | ❌ Lost | -$3.25 |
| 9/28 9:46:04 PM | Gold | DOWN | 13.9 min | 59¢ | 66% | 5¢ | ✅ Won | $3.93 |
| 9/28 9:32:24 PM | Silver | DOWN | 12.6 min | 42¢ | 48% | 4¢ | ✅ Won | $5.62 |
| 9/28 9:32:08 PM | Gold | UP | 12.8 min | 42¢ | 52% | 8¢ | ❌ Lost | -$4.38 |
| 9/28 9:18:13 PM | Gold | DOWN | 11.8 min | 35¢ | 42% | 6¢ | ❌ Lost | -$3.66 |
| 9/28 9:16:07 PM | Silver | DOWN | 13.9 min | 29¢ | 37% | 6¢ | ❌ Lost | -$3.05 |
| 9/28 9:02:38 PM | Silver | DOWN | 12.4 min | 34¢ | 41% | 5¢ | ✅ Won | $6.44 |
| 9/28 9:01:26 PM | Gold | DOWN | 13.6 min | 42¢ | 49% | 5¢ | ✅ Won | $5.62 |

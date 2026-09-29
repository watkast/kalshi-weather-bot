# Gold & Silver Fair-Value Bot

*Updated Mon Sep 28, 9:00 PM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

⏳ **Too early.** 12 of 30 settled trades needed before judging.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 14 | 12 | 5 (42%) | 36¢ | 45% | $4.50 | +10% |
| Silver | 7 | 6 | 1 (17%) | 30¢ | 38% | -$9.06 | -48% |
| Gold | 7 | 6 | 4 (67%) | 42¢ | 51% | $13.56 | +51% |

*Earlier half $7.42 / later half -$2.92.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 12 | 6 (50%) | $7.43 | +14% |
| 4¢+ ← live bot | 12 | 5 (42%) | $7.42 | +17% |
| 6¢+ | 12 | 4 (33%) | $2.04 | +5% |
| 8¢+ | 11 | 5 (45%) | $19.11 | +62% |
| 10¢+ | 10 | 2 (20%) | -$0.91 | -4% |
| 15¢+ | 4 | 2 (50%) | $11.44 | +134% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 296 | -0.1% |
| Hyperliquid price vs Kalshi's target | 296 | +7.8% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 8:46:49 PM | Gold | UP | 13.2 min | 50¢ | 56% | 4¢ | Open | — |
| 9/28 8:46:37 PM | Silver | DOWN | 13.4 min | 30¢ | 38% | 7¢ | Open | — |
| 9/28 8:39:44 PM | Silver | UP | 5.3 min | 9¢ | 16% | 6¢ | ❌ Lost | -$0.95 |
| 9/28 8:31:02 PM | Gold | UP | 14.0 min | 53¢ | 61% | 6¢ | ✅ Won | $4.52 |
| 9/28 8:18:20 PM | Silver | DOWN | 11.7 min | 39¢ | 48% | 7¢ | ❌ Lost | -$4.07 |
| 9/28 8:17:38 PM | Gold | UP | 12.4 min | 45¢ | 51% | 5¢ | ✅ Won | $5.32 |
| 9/28 8:01:29 PM | Gold | UP | 13.5 min | 32¢ | 43% | 10¢ | ❌ Lost | -$3.36 |
| 9/28 8:01:07 PM | Silver | UP | 13.9 min | 42¢ | 48% | 4¢ | ❌ Lost | -$4.38 |
| 9/28 7:47:42 PM | Silver | UP | 12.3 min | 30¢ | 37% | 5¢ | ❌ Lost | -$3.15 |
| 9/28 7:46:12 PM | Gold | DOWN | 13.8 min | 44¢ | 51% | 5¢ | ❌ Lost | -$4.58 |
| 9/28 7:32:13 PM | Silver | UP | 12.8 min | 33¢ | 41% | 6¢ | ✅ Won | $6.54 |
| 9/28 7:31:57 PM | Gold | UP | 13.1 min | 35¢ | 45% | 8¢ | ✅ Won | $6.34 |

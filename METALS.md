# Gold & Silver Fair-Value Bot

*Updated Mon Sep 28, 10:10 PM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

⏳ **Too early.** 22 of 30 settled trades needed before judging.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 24 | 22 | 11 (50%) | 38¢ | 46% | $23.44 | +27% |
| Silver | 12 | 11 | 4 (36%) | 32¢ | 40% | $3.55 | +10% |
| Gold | 12 | 11 | 7 (64%) | 44¢ | 52% | $19.89 | +40% |

*Earlier half $5.45 / later half $17.99.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 22 | 9 (41%) | -$4.78 | -5% |
| 4¢+ ← live bot | 21 | 9 (43%) | $11.30 | +14% |
| 6¢+ | 21 | 8 (38%) | $13.21 | +20% |
| 8¢+ | 20 | 8 (40%) | $25.67 | +47% |
| 10¢+ | 18 | 5 (28%) | $8.67 | +21% |
| 15¢+ | 9 | 4 (44%) | $20.38 | +104% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 547 | -0.8% |
| Hyperliquid price vs Kalshi's target | 547 | -6.4% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 10:01:37 PM | Silver | UP | 13.4 min | 32¢ | 39% | 5¢ | Open | — |
| 9/28 10:01:05 PM | Gold | UP | 13.9 min | 36¢ | 43% | 5¢ | Open | — |
| 9/28 9:51:10 PM | Silver | UP | 8.8 min | 31¢ | 41% | 9¢ | ❌ Lost | -$3.25 |
| 9/28 9:46:04 PM | Gold | DOWN | 13.9 min | 59¢ | 66% | 5¢ | ✅ Won | $3.93 |
| 9/28 9:32:24 PM | Silver | DOWN | 12.6 min | 42¢ | 48% | 4¢ | ✅ Won | $5.62 |
| 9/28 9:32:08 PM | Gold | UP | 12.8 min | 42¢ | 52% | 8¢ | ❌ Lost | -$4.38 |
| 9/28 9:18:13 PM | Gold | DOWN | 11.8 min | 35¢ | 42% | 6¢ | ❌ Lost | -$3.66 |
| 9/28 9:16:07 PM | Silver | DOWN | 13.9 min | 29¢ | 37% | 6¢ | ❌ Lost | -$3.05 |
| 9/28 9:02:38 PM | Silver | DOWN | 12.4 min | 34¢ | 41% | 5¢ | ✅ Won | $6.44 |
| 9/28 9:01:26 PM | Gold | DOWN | 13.6 min | 42¢ | 49% | 5¢ | ✅ Won | $5.62 |
| 9/28 8:46:49 PM | Gold | UP | 13.2 min | 50¢ | 56% | 4¢ | ✅ Won | $4.82 |
| 9/28 8:46:37 PM | Silver | DOWN | 13.4 min | 30¢ | 38% | 7¢ | ✅ Won | $6.85 |

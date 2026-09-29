# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 3:22 PM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 124 | 123 | 43 (35%) | 39¢ | 47% | -$63.50 | -13% |
| Silver | 62 | 62 | 20 (32%) | 33¢ | 41% | -$15.52 | -7% |
| Gold | 62 | 61 | 23 (38%) | 44¢ | 52% | -$47.98 | -17% |

*Earlier half -$24.72 / later half -$38.78.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 126 | 43 (34%) | -$91.49 | -18% |
| 4¢+ ← live bot | 123 | 45 (37%) | -$10.77 | -2% |
| 6¢+ | 111 | 48 (43%) | $96.74 | +25% |
| 8¢+ | 98 | 41 (42%) | $101.86 | +33% |
| 10¢+ | 85 | 32 (38%) | $65.41 | +26% |
| 15¢+ | 52 | 19 (37%) | $56.38 | +42% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 3144 | -2.2% |
| Hyperliquid price vs Kalshi's target | 3144 | +1.7% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 3:16:35 PM | Gold | DOWN | 13.4 min | 47¢ | 53% | 4¢ | Open | — |
| 9/29 3:02:32 PM | Gold | DOWN | 12.5 min | 41¢ | 52% | 9¢ | ✅ Won | $5.73 |
| 9/29 3:01:02 PM | Silver | DOWN | 13.9 min | 14¢ | 49% | 34¢ | ❌ Lost | -$1.49 |
| 9/29 2:46:28 PM | Silver | UP | 13.5 min | 30¢ | 37% | 5¢ | ❌ Lost | -$3.15 |
| 9/29 2:46:03 PM | Gold | UP | 13.9 min | 32¢ | 52% | 18¢ | ❌ Lost | -$3.36 |
| 9/29 2:32:20 PM | Silver | DOWN | 12.7 min | 28¢ | 35% | 5¢ | ❌ Lost | -$2.95 |
| 9/29 2:31:04 PM | Gold | UP | 13.9 min | 41¢ | 50% | 7¢ | ✅ Won | $5.73 |
| 9/29 2:17:22 PM | Gold | DOWN | 12.6 min | 50¢ | 56% | 5¢ | ❌ Lost | -$5.18 |
| 9/29 2:16:04 PM | Silver | UP | 13.9 min | 30¢ | 38% | 7¢ | ✅ Won | $6.85 |
| 9/29 2:02:20 PM | Silver | UP | 12.7 min | 19¢ | 25% | 4¢ | ❌ Lost | -$2.01 |
| 9/29 2:01:04 PM | Gold | UP | 13.9 min | 43¢ | 57% | 12¢ | ❌ Lost | -$4.48 |
| 9/29 1:49:06 PM | Silver | UP | 10.9 min | 34¢ | 41% | 5¢ | ✅ Won | $6.44 |

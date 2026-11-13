# Range-Scalp Bot

*Updated Fri Nov 13 20:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58579 | 51113 | 7466 (105) | 7 | $-15803.14 | -4.3% |
| **+10¢** | 43759 | 35027 | 8732 (139) | 7 | $-14777.14 | -5.4% |
| **+15¢** | 36674 | 27269 | 9405 (174) | 8 | $-13364.03 | -5.8% |
| **+20¢** | 32672 | 22799 | 9873 (225) | 8 | $-11740.23 | -5.7% |
| **+10¢ (15¢ stop)** | 71343 | 71209 | 134 (82) | 0 | $-26264.42 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 20:10 | +10 stop | HYPE | UP | 0.69 | 0.84 | 1.25 |
| 11-13 20:09 | +10 stop | DOGE | UP | 0.48 | 0.60 | 0.84 |
| 11-13 20:09 | +10 | DOGE | UP | 0.48 | 0.60 | 0.84 |
| 11-13 20:09 | +5 | DOGE | UP | 0.48 | 0.60 | 0.85 |
| 11-13 20:09 | +10 stop | BNB | UP | 0.67 | 0.78 | 0.81 |
| 11-13 20:09 | +10 stop | BTC | UP | 0.64 | 0.74 | 0.69 |
| 11-13 20:08 | +10 stop | DOGE | DOWN | 0.54 | 0.68 | 1.06 |
| 11-13 20:08 | +10 | DOGE | DOWN | 0.54 | 0.68 | 1.06 |
| 11-13 20:08 | +5 | DOGE | DOWN | 0.54 | 0.68 | 1.06 |
| 11-13 20:08 | +10 stop | BNB | DOWN | 0.64 | 0.45 | -2.25 |
| 11-13 20:08 | +5 | BNB | DOWN | 0.64 | open |  |
| 11-13 20:07 | +10 stop | ETH | DOWN | 0.61 | 0.42 | -2.25 |
| 11-13 20:07 | +10 stop | BTC | DOWN | 0.64 | 0.43 | -2.45 |
| 11-13 20:07 | +10 | BTC | DOWN | 0.64 | open |  |
| 11-13 20:07 | +5 | BTC | DOWN | 0.64 | open |  |
| 11-13 20:07 | +10 stop | NEAR | DOWN | 0.60 | 0.41 | -2.24 |
| 11-13 20:07 | +5 | NEAR | DOWN | 0.60 | open |  |
| 11-13 20:07 | +10 stop | HYPE | DOWN | 0.66 | 0.40 | -2.93 |
| 11-13 20:07 | +20 | HYPE | DOWN | 0.66 | open |  |
| 11-13 20:07 | +15 | HYPE | DOWN | 0.66 | open |  |
| 11-13 20:07 | +10 | HYPE | DOWN | 0.66 | open |  |
| 11-13 20:07 | +5 | HYPE | DOWN | 0.66 | open |  |
| 11-13 20:06 | +10 stop | NEAR | DOWN | 0.65 | 0.77 | 0.91 |
| 11-13 20:06 | +10 stop | XRP | UP | 0.55 | 0.66 | 0.76 |
| 11-13 20:06 | +5 | NEAR | DOWN | 0.65 | 0.72 | 0.39 |
| 11-13 20:06 | +10 stop | ETH | DOWN | 0.58 | 0.74 | 1.25 |
| 11-13 20:04 | +5 | ETH | DOWN | 0.70 | open |  |
| 11-13 20:04 | +10 stop | SOL | UP | 0.66 | 0.80 | 1.12 |
| 11-13 20:04 | +5 | XRP | DOWN | 0.65 | open |  |
| 11-13 20:04 | +5 | BTC | DOWN | 0.62 | 0.76 | 1.10 |
| 11-13 20:04 | +10 stop | DOGE | DOWN | 0.68 | 0.50 | -2.14 |
| 11-13 20:04 | +20 | DOGE | DOWN | 0.68 | open |  |
| 11-13 20:04 | +15 | DOGE | DOWN | 0.68 | open |  |
| 11-13 20:04 | +10 | DOGE | DOWN | 0.68 | 0.79 | 0.82 |
| 11-13 20:04 | +5 | DOGE | DOWN | 0.68 | 0.79 | 0.82 |
| 11-13 20:03 | +10 stop | NEAR | DOWN | 0.69 | 0.53 | -1.93 |
| 11-13 20:03 | +20 | NEAR | DOWN | 0.69 | open |  |
| 11-13 20:03 | +15 | NEAR | DOWN | 0.69 | open |  |
| 11-13 20:03 | +10 | NEAR | DOWN | 0.69 | open |  |
| 11-13 20:03 | +5 | NEAR | DOWN | 0.69 | 0.75 | 0.31 |

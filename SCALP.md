# Range-Scalp Bot

*Updated Tue Nov 17 15:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62950 | 54905 | 8045 (117) | 0 | $-17182.41 | -4.3% |
| **+10¢** | 47017 | 37604 | 9413 (159) | 0 | $-16059.67 | -5.4% |
| **+15¢** | 39409 | 29259 | 10150 (201) | 0 | $-14584.41 | -5.9% |
| **+20¢** | 35119 | 24476 | 10643 (256) | 1 | $-12758.20 | -5.8% |
| **+10¢ (15¢ stop)** | 76600 | 76444 | 156 (92) | 0 | $-28222.28 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 15:31 | +5 | BNB | DOWN | 0.70 | 0.75 | 0.21 |
| 11-17 15:31 | +10 stop | BNB | DOWN | 0.71 | 0.85 | 1.16 |
| 11-17 15:31 | +20 | BNB | DOWN | 0.71 | open |  |
| 11-17 15:31 | +15 | BNB | DOWN | 0.71 | 0.86 | 1.26 |
| 11-17 15:31 | +10 | BNB | DOWN | 0.71 | 0.85 | 1.16 |
| 11-17 15:31 | +10 stop | HYPE | DOWN | 0.70 | 0.88 | 1.58 |
| 11-17 15:31 | +20 | HYPE | DOWN | 0.68 | 0.88 | 1.76 |
| 11-17 15:31 | +15 | HYPE | DOWN | 0.64 | 0.88 | 2.15 |
| 11-17 15:31 | +10 | HYPE | DOWN | 0.71 | 0.88 | 1.48 |
| 11-17 15:31 | +5 | HYPE | DOWN | 0.71 | 0.78 | 0.43 |
| 11-17 15:31 | +10 stop | SOL | DOWN | 0.70 | 0.87 | 1.47 |
| 11-17 15:31 | +20 | SOL | DOWN | 0.69 | 0.92 | 2.05 |
| 11-17 15:31 | +15 | SOL | DOWN | 0.69 | 0.87 | 1.57 |
| 11-17 15:31 | +10 | SOL | DOWN | 0.70 | 0.87 | 1.47 |
| 11-17 15:31 | +5 | SOL | DOWN | 0.70 | 0.78 | 0.52 |
| 11-17 15:31 | +10 stop | BTC | DOWN | 0.65 | 0.81 | 1.33 |
| 11-17 15:31 | +20 | BTC | DOWN | 0.65 | 0.85 | 1.75 |
| 11-17 15:31 | +15 | BTC | DOWN | 0.65 | 0.81 | 1.33 |
| 11-17 15:31 | +10 | BTC | DOWN | 0.65 | 0.81 | 1.33 |
| 11-17 15:31 | +5 | BTC | DOWN | 0.65 | 0.73 | 0.50 |
| 11-17 15:19 | +10 stop | ZEC | UP | 0.65 | 0.86 | 1.83 |
| 11-17 15:19 | +5 | ZEC | UP | 0.66 | 0.73 | 0.40 |
| 11-17 15:19 | +10 stop | BTC | UP | 0.64 | 0.74 | 0.69 |
| 11-17 15:19 | +10 stop | ETH | UP | 0.53 | 0.66 | 0.96 |
| 11-17 15:19 | +10 stop | BNB | UP | 0.69 | 0.86 | 1.46 |
| 11-17 15:19 | +10 stop | HYPE | UP | 0.69 | 0.83 | 1.15 |
| 11-17 15:19 | +10 | HYPE | UP | 0.69 | 0.83 | 1.15 |
| 11-17 15:19 | +5 | HYPE | UP | 0.69 | 0.78 | 0.62 |
| 11-17 15:19 | +10 stop | XRP | UP | 0.68 | 0.78 | 0.74 |
| 11-17 15:19 | +10 stop | DOGE | UP | 0.68 | 0.79 | 0.82 |
| 11-17 15:19 | +10 stop | NEAR | UP | 0.68 | 0.80 | 0.93 |
| 11-17 15:18 | +10 stop | HYPE | UP | 0.52 | 0.65 | 0.96 |
| 11-17 15:18 | +20 | HYPE | UP | 0.52 | 0.73 | 1.78 |
| 11-17 15:18 | +15 | HYPE | UP | 0.52 | 0.71 | 1.57 |
| 11-17 15:18 | +10 | HYPE | UP | 0.52 | 0.65 | 0.96 |
| 11-17 15:18 | +5 | HYPE | UP | 0.52 | 0.65 | 0.96 |
| 11-17 15:17 | +10 stop | BNB | DOWN | 0.58 | 0.41 | -2.06 |
| 11-17 15:17 | +20 | BNB | DOWN | 0.58 | yes | -5.99 |
| 11-17 15:17 | +15 | BNB | DOWN | 0.58 | yes | -5.99 |
| 11-17 15:17 | +10 | BNB | DOWN | 0.58 | yes | -5.99 |

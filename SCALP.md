# Range-Scalp Bot

*Updated Thu Nov 12 21:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57293 | 49955 | 7338 (101) | 2 | $-15690.76 | -4.4% |
| **+10¢** | 42823 | 34257 | 8566 (133) | 2 | $-14632.98 | -5.4% |
| **+15¢** | 35903 | 26683 | 9220 (167) | 2 | $-13223.70 | -5.9% |
| **+20¢** | 31987 | 22313 | 9674 (217) | 3 | $-11584.43 | -5.8% |
| **+10¢ (15¢ stop)** | 69861 | 69733 | 128 (78) | 0 | $-25755.04 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 21:11 | +10 stop | BTC | UP | 0.56 | 0.90 | 3.18 |
| 11-12 21:10 | +10 stop | NEAR | DOWN | 0.68 | 0.78 | 0.71 |
| 11-12 21:09 | +10 stop | DOGE | DOWN | 0.68 | 0.52 | -1.94 |
| 11-12 21:09 | +5 | DOGE | DOWN | 0.66 | 0.73 | 0.40 |
| 11-12 21:08 | +10 stop | DOGE | DOWN | 0.57 | 0.68 | 0.74 |
| 11-12 21:08 | +5 | DOGE | DOWN | 0.57 | 0.65 | 0.44 |
| 11-12 21:08 | +10 stop | NEAR | DOWN | 0.43 | 0.54 | 0.74 |
| 11-12 21:08 | +10 stop | BTC | DOWN | 0.68 | 0.47 | -2.44 |
| 11-12 21:08 | +5 | BTC | DOWN | 0.68 | open |  |
| 11-12 21:08 | +10 stop | BNB | UP | 0.54 | 0.69 | 1.17 |
| 11-12 21:07 | +10 stop | NEAR | DOWN | 0.57 | 0.71 | 1.07 |
| 11-12 21:06 | +10 stop | XRP | DOWN | 0.58 | 0.41 | -2.05 |
| 11-12 21:06 | +10 stop | BNB | DOWN | 0.63 | 0.43 | -2.35 |
| 11-12 21:05 | +5 | DOGE | DOWN | 0.65 | 0.72 | 0.39 |
| 11-12 21:05 | +10 stop | ZEC | DOWN | 0.70 | 0.91 | 1.87 |
| 11-12 21:05 | +5 | DOGE | DOWN | 0.46 | 0.59 | 0.95 |
| 11-12 21:04 | +10 stop | SOL | DOWN | 0.60 | 0.78 | 1.50 |
| 11-12 21:04 | +10 stop | NEAR | DOWN | 0.60 | 0.76 | 1.30 |
| 11-12 21:04 | +5 | SOL | DOWN | 0.69 | 0.78 | 0.62 |
| 11-12 21:04 | +10 stop | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 11-12 21:04 | +15 | ETH | DOWN | 0.63 | 0.81 | 1.52 |
| 11-12 21:04 | +10 | ETH | DOWN | 0.63 | 0.76 | 1.00 |
| 11-12 21:04 | +5 | ETH | DOWN | 0.63 | 0.68 | 0.17 |
| 11-12 21:04 | +5 | HYPE | DOWN | 0.64 | 0.72 | 0.48 |
| 11-12 21:04 | +10 stop | XRP | UP | 0.56 | 0.31 | -2.83 |
| 11-12 21:03 | +10 stop | BTC | DOWN | 0.52 | 0.62 | 0.65 |
| 11-12 21:03 | +5 | ZEC | DOWN | 0.67 | 0.75 | 0.50 |
| 11-12 21:03 | +10 stop | HYPE | UP | 0.48 | 0.33 | -1.84 |
| 11-12 21:03 | +15 | HYPE | UP | 0.48 | 0.71 | 1.97 |
| 11-12 21:03 | +10 | HYPE | UP | 0.48 | 0.71 | 2.01 |
| 11-12 21:03 | +5 | HYPE | UP | 0.47 | 0.57 | 0.64 |
| 11-12 21:03 | +5 | BTC | DOWN | 0.55 | 0.62 | 0.35 |
| 11-12 21:03 | +10 stop | BNB | UP | 0.66 | 0.50 | -1.94 |
| 11-12 21:03 | +5 | BNB | UP | 0.67 | 0.76 | 0.62 |
| 11-12 21:03 | +10 stop | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 11-12 21:03 | +5 | DOGE | DOWN | 0.63 | 0.68 | 0.17 |
| 11-12 21:03 | +10 stop | NEAR | UP | 0.61 | 0.45 | -1.95 |
| 11-12 21:03 | +20 | NEAR | UP | 0.61 | open |  |
| 11-12 21:03 | +15 | NEAR | UP | 0.61 | open |  |
| 11-12 21:03 | +10 | NEAR | UP | 0.61 | open |  |

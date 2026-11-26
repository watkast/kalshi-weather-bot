# Range-Scalp Bot

*Updated Thu Nov 26 01:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 72112 | 62951 | 9161 (158) | 3 | $-19127.26 | -4.2% |
| **+10¢** | 53797 | 43096 | 10701 (203) | 3 | $-17733.22 | -5.2% |
| **+15¢** | 45042 | 33516 | 11526 (260) | 3 | $-15820.34 | -5.6% |
| **+20¢** | 40101 | 27962 | 12139 (326) | 3 | $-14208.74 | -5.6% |
| **+10¢ (15¢ stop)** | 87778 | 87569 | 209 (128) | 0 | $-32156.62 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-26 01:12 | +10 stop | HYPE | DOWN | 0.66 | 0.82 | 1.33 |
| 11-26 01:12 | +10 | HYPE | DOWN | 0.66 | 0.82 | 1.33 |
| 11-26 01:12 | +5 | HYPE | DOWN | 0.66 | 0.72 | 0.29 |
| 11-26 01:11 | +10 stop | SOL | UP | 0.62 | 0.74 | 0.89 |
| 11-26 01:09 | +5 | HYPE | DOWN | 0.51 | 0.59 | 0.45 |
| 11-26 01:09 | +10 stop | HYPE | DOWN | 0.56 | 0.71 | 1.17 |
| 11-26 01:09 | +15 | HYPE | DOWN | 0.57 | 0.72 | 1.17 |
| 11-26 01:09 | +10 | HYPE | DOWN | 0.56 | 0.71 | 1.17 |
| 11-26 01:09 | +5 | HYPE | DOWN | 0.56 | 0.62 | 0.25 |
| 11-26 01:08 | +10 stop | BTC | UP | 0.68 | 0.78 | 0.71 |
| 11-26 01:08 | +5 | BTC | UP | 0.68 | 0.73 | 0.20 |
| 11-26 01:08 | +5 | BNB | UP | 0.59 | 0.65 | 0.27 |
| 11-26 01:08 | +10 stop | DOGE | UP | 0.59 | 0.69 | 0.68 |
| 11-26 01:08 | +10 stop | BNB | UP | 0.54 | 0.65 | 0.76 |
| 11-26 01:07 | +10 stop | ETH | UP | 0.67 | 0.88 | 1.86 |
| 11-26 01:07 | +5 | HYPE | DOWN | 0.60 | 0.69 | 0.58 |
| 11-26 01:07 | +10 stop | BTC | UP | 0.63 | 0.73 | 0.69 |
| 11-26 01:07 | +20 | BTC | UP | 0.64 | 0.85 | 1.84 |
| 11-26 01:07 | +15 | BTC | UP | 0.64 | 0.85 | 1.84 |
| 11-26 01:07 | +10 | BTC | UP | 0.64 | 0.78 | 1.10 |
| 11-26 01:07 | +5 | BTC | UP | 0.64 | 0.73 | 0.59 |
| 11-26 01:07 | +10 stop | HYPE | DOWN | 0.63 | 0.73 | 0.69 |
| 11-26 01:07 | +10 stop | NEAR | DOWN | 0.67 | 0.49 | -2.13 |
| 11-26 01:07 | +20 | NEAR | DOWN | 0.67 | open |  |
| 11-26 01:07 | +15 | NEAR | DOWN | 0.67 | open |  |
| 11-26 01:07 | +5 | NEAR | DOWN | 0.67 | open |  |
| 11-26 01:06 | +5 | BNB | UP | 0.53 | 0.63 | 0.65 |
| 11-26 01:06 | +5 | XRP | UP | 0.71 | 0.81 | 0.74 |
| 11-26 01:06 | +10 | NEAR | DOWN | 0.66 | open |  |
| 11-26 01:05 | +10 stop | HYPE | UP | 0.57 | 0.36 | -2.45 |
| 11-26 01:05 | +10 stop | DOGE | UP | 0.68 | 0.53 | -1.84 |
| 11-26 01:05 | +10 stop | ZEC | UP | 0.64 | 0.40 | -2.70 |
| 11-26 01:05 | +10 | NEAR | DOWN | 0.45 | 0.55 | 0.67 |
| 11-26 01:05 | +10 stop | ETH | UP | 0.71 | 0.50 | -2.43 |
| 11-26 01:05 | +10 | ETH | UP | 0.71 | 0.88 | 1.47 |
| 11-26 01:05 | +5 | ETH | UP | 0.71 | 0.88 | 1.47 |
| 11-26 01:05 | +5 | NEAR | DOWN | 0.54 | 0.67 | 0.97 |
| 11-26 01:05 | +10 stop | BNB | UP | 0.63 | 0.48 | -1.85 |
| 11-26 01:05 | +20 | BNB | UP | 0.63 | 0.87 | 2.15 |
| 11-26 01:05 | +15 | BNB | UP | 0.63 | 0.87 | 2.15 |

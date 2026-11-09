# Range-Scalp Bot

*Updated Mon Nov 09 06:17 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53415 | 46573 | 6842 (85) | 0 | $-14757.03 | -4.4% |
| **+10¢** | 39899 | 31918 | 7981 (110) | 0 | $-13762.18 | -5.5% |
| **+15¢** | 33433 | 24833 | 8600 (141) | 1 | $-12564.56 | -6.0% |
| **+20¢** | 29749 | 20731 | 9018 (186) | 1 | $-11063.20 | -5.9% |
| **+10¢ (15¢ stop)** | 65090 | 64984 | 106 (63) | 0 | $-24116.07 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 06:15 | +10 stop | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 11-09 06:15 | +20 | SOL | DOWN | 0.70 | open |  |
| 11-09 06:15 | +15 | SOL | DOWN | 0.70 | open |  |
| 11-09 06:15 | +10 | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 11-09 06:15 | +5 | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 11-09 06:14 | +10 stop | NEAR | UP | 0.05 | 0.56 | 4.90 |
| 11-09 06:14 | +20 | NEAR | UP | 0.05 | 0.56 | 4.90 |
| 11-09 06:14 | +15 | NEAR | UP | 0.05 | 0.56 | 4.89 |
| 11-09 06:14 | +10 | NEAR | UP | 0.05 | 0.56 | 4.89 |
| 11-09 06:14 | +5 | NEAR | UP | 0.05 | 0.56 | 4.88 |
| 11-09 06:13 | +10 stop | SOL | UP | 0.32 | 0.64 | 2.87 |
| 11-09 06:12 | +10 stop | NEAR | UP | 0.25 | 0.56 | 2.78 |
| 11-09 06:12 | +20 | NEAR | UP | 0.25 | 0.56 | 2.78 |
| 11-09 06:12 | +15 | NEAR | UP | 0.25 | 0.56 | 2.78 |
| 11-09 06:12 | +10 | NEAR | UP | 0.25 | 0.56 | 2.78 |
| 11-09 06:12 | +5 | NEAR | UP | 0.25 | 0.56 | 2.78 |
| 11-09 06:11 | +10 stop | SOL | DOWN | 0.68 | 0.53 | -1.84 |
| 11-09 06:11 | +15 | SOL | DOWN | 0.68 | 0.88 | 1.76 |
| 11-09 06:11 | +10 | SOL | DOWN | 0.68 | 0.88 | 1.76 |
| 11-09 06:11 | +5 | SOL | DOWN | 0.68 | 0.88 | 1.76 |
| 11-09 06:11 | +10 stop | BNB | DOWN | 0.66 | 0.77 | 0.81 |
| 11-09 06:11 | +15 | BNB | DOWN | 0.66 | 0.97 | 2.90 |
| 11-09 06:11 | +10 | BNB | DOWN | 0.66 | 0.77 | 0.81 |
| 11-09 06:11 | +5 | BNB | DOWN | 0.66 | 0.71 | 0.19 |
| 11-09 06:11 | +5 | DOGE | UP | 0.62 | 0.75 | 0.99 |
| 11-09 06:11 | +10 stop | DOGE | UP | 0.57 | 0.75 | 1.48 |
| 11-09 06:11 | +10 | DOGE | UP | 0.57 | 0.75 | 1.48 |
| 11-09 06:11 | +10 stop | HYPE | UP | 0.56 | 0.84 | 2.49 |
| 11-09 06:10 | +10 stop | HYPE | DOWN | 0.43 | 0.53 | 0.64 |
| 11-09 06:10 | +10 stop | ETH | UP | 0.64 | 0.80 | 1.31 |
| 11-09 06:10 | +20 | ETH | UP | 0.64 | 0.90 | 2.39 |
| 11-09 06:10 | +15 | ETH | UP | 0.64 | 0.80 | 1.31 |
| 11-09 06:09 | +10 stop | DOGE | UP | 0.52 | 0.34 | -2.14 |
| 11-09 06:09 | +20 | DOGE | UP | 0.53 | 0.75 | 1.88 |
| 11-09 06:09 | +15 | DOGE | UP | 0.53 | 0.75 | 1.88 |
| 11-09 06:09 | +5 | DOGE | UP | 0.53 | 0.63 | 0.65 |
| 11-09 06:09 | +10 stop | NEAR | UP | 0.46 | 0.56 | 0.64 |
| 11-09 06:09 | +20 | NEAR | UP | 0.46 | 0.68 | 1.86 |
| 11-09 06:09 | +15 | NEAR | UP | 0.46 | 0.68 | 1.86 |
| 11-09 06:09 | +5 | NEAR | UP | 0.46 | 0.56 | 0.64 |

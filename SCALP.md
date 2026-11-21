# Range-Scalp Bot

*Updated Sat Nov 21 06:17 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 67162 | 58619 | 8543 (129) | 2 | $-18024.70 | -4.3% |
| **+10¢** | 50155 | 40169 | 9986 (171) | 3 | $-16754.53 | -5.3% |
| **+15¢** | 42057 | 31294 | 10763 (219) | 5 | $-15017.83 | -5.7% |
| **+20¢** | 37432 | 26122 | 11310 (276) | 5 | $-13352.51 | -5.7% |
| **+10¢ (15¢ stop)** | 81768 | 81602 | 166 (100) | 2 | $-30090.80 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 06:17 | +10 stop | NEAR | UP | 0.65 | open |  |
| 11-21 06:17 | +20 | NEAR | UP | 0.65 | open |  |
| 11-21 06:17 | +15 | NEAR | UP | 0.65 | open |  |
| 11-21 06:17 | +10 | NEAR | UP | 0.65 | open |  |
| 11-21 06:17 | +5 | NEAR | UP | 0.65 | open |  |
| 11-21 06:17 | +10 stop | BNB | UP | 0.59 | open |  |
| 11-21 06:17 | +20 | BNB | UP | 0.60 | open |  |
| 11-21 06:17 | +15 | BNB | UP | 0.60 | open |  |
| 11-21 06:17 | +10 | BNB | UP | 0.62 | open |  |
| 11-21 06:17 | +5 | BNB | UP | 0.62 | open |  |
| 11-21 06:17 | +10 stop | NEAR | DOWN | 0.45 | 0.67 | 1.86 |
| 11-21 06:17 | +20 | NEAR | DOWN | 0.46 | 0.67 | 1.80 |
| 11-21 06:17 | +15 | NEAR | DOWN | 0.44 | 0.67 | 1.95 |
| 11-21 06:17 | +10 | NEAR | DOWN | 0.44 | 0.67 | 1.96 |
| 11-21 06:17 | +5 | NEAR | DOWN | 0.43 | 0.67 | 2.05 |
| 11-21 06:16 | +10 stop | SOL | DOWN | 0.59 | 0.69 | 0.68 |
| 11-21 06:16 | +20 | SOL | DOWN | 0.59 | open |  |
| 11-21 06:16 | +15 | SOL | DOWN | 0.58 | open |  |
| 11-21 06:16 | +10 | SOL | DOWN | 0.59 | 0.69 | 0.68 |
| 11-21 06:16 | +5 | SOL | DOWN | 0.58 | 0.67 | 0.56 |
| 11-21 06:16 | +10 stop | ETH | DOWN | 0.70 | 0.48 | -2.53 |
| 11-21 06:16 | +20 | ETH | DOWN | 0.70 | open |  |
| 11-21 06:16 | +15 | ETH | DOWN | 0.71 | open |  |
| 11-21 06:16 | +10 | ETH | DOWN | 0.71 | open |  |
| 11-21 06:16 | +5 | ETH | DOWN | 0.71 | 0.79 | 0.53 |
| 11-21 06:16 | +10 stop | XRP | DOWN | 0.68 | 0.82 | 1.13 |
| 11-21 06:16 | +20 | XRP | DOWN | 0.69 | open |  |
| 11-21 06:16 | +15 | XRP | DOWN | 0.69 | open |  |
| 11-21 06:16 | +10 | XRP | DOWN | 0.70 | 0.82 | 0.94 |
| 11-21 06:16 | +5 | XRP | DOWN | 0.70 | 0.82 | 0.94 |
| 11-21 06:11 | +15 | SOL | DOWN | 0.65 | 0.84 | 1.64 |
| 11-21 06:11 | +10 | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 11-21 06:11 | +5 | BTC | DOWN | 0.70 | 0.87 | 1.47 |
| 11-21 06:10 | +10 stop | SOL | DOWN | 0.70 | 0.31 | -4.20 |
| 11-21 06:10 | +5 | SOL | DOWN | 0.70 | 0.75 | 0.21 |
| 11-21 06:10 | +10 stop | ETH | DOWN | 0.66 | 0.84 | 1.54 |
| 11-21 06:09 | +10 stop | XRP | DOWN | 0.57 | 0.74 | 1.38 |
| 11-21 06:09 | +20 | XRP | DOWN | 0.57 | 0.81 | 2.11 |
| 11-21 06:09 | +15 | XRP | DOWN | 0.57 | 0.74 | 1.38 |
| 11-21 06:09 | +10 | XRP | DOWN | 0.56 | 0.74 | 1.48 |

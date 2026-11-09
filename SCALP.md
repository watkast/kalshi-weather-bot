# Range-Scalp Bot

*Updated Mon Nov 09 06:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53419 | 46577 | 6842 (85) | 0 | $-14754.94 | -4.4% |
| **+10¢** | 39902 | 31921 | 7981 (110) | 1 | $-13759.35 | -5.5% |
| **+15¢** | 33436 | 24836 | 8600 (141) | 1 | $-12560.23 | -6.0% |
| **+20¢** | 29750 | 20732 | 9018 (186) | 3 | $-11061.35 | -5.9% |
| **+10¢ (15¢ stop)** | 65095 | 64989 | 106 (63) | 0 | $-24116.35 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 06:26 | +10 stop | NEAR | DOWN | 0.44 | 0.69 | 2.17 |
| 11-09 06:24 | +10 stop | ZEC | DOWN | 0.59 | 0.70 | 0.78 |
| 11-09 06:24 | +20 | ZEC | DOWN | 0.59 | open |  |
| 11-09 06:24 | +15 | ZEC | DOWN | 0.59 | 0.75 | 1.29 |
| 11-09 06:24 | +10 | ZEC | DOWN | 0.59 | 0.70 | 0.78 |
| 11-09 06:24 | +5 | ZEC | DOWN | 0.59 | 0.67 | 0.47 |
| 11-09 06:24 | +10 stop | NEAR | DOWN | 0.71 | 0.56 | -1.83 |
| 11-09 06:24 | +20 | NEAR | DOWN | 0.71 | open |  |
| 11-09 06:24 | +15 | NEAR | DOWN | 0.71 | open |  |
| 11-09 06:24 | +10 | NEAR | DOWN | 0.71 | open |  |
| 11-09 06:24 | +5 | NEAR | DOWN | 0.71 | 0.79 | 0.53 |
| 11-09 06:23 | +10 stop | HYPE | DOWN | 0.64 | 0.44 | -2.35 |
| 11-09 06:23 | +10 | HYPE | DOWN | 0.64 | 0.78 | 1.10 |
| 11-09 06:23 | +5 | HYPE | DOWN | 0.64 | 0.71 | 0.38 |
| 11-09 06:20 | +10 stop | HYPE | DOWN | 0.69 | 0.81 | 0.95 |
| 11-09 06:20 | +20 | HYPE | DOWN | 0.69 | open |  |
| 11-09 06:20 | +15 | HYPE | DOWN | 0.69 | 0.87 | 1.57 |
| 11-09 06:20 | +10 | HYPE | DOWN | 0.69 | 0.81 | 0.95 |
| 11-09 06:20 | +5 | HYPE | DOWN | 0.68 | 0.78 | 0.71 |
| 11-09 06:15 | +10 stop | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 11-09 06:15 | +20 | SOL | DOWN | 0.70 | 0.91 | 1.85 |
| 11-09 06:15 | +15 | SOL | DOWN | 0.70 | 0.87 | 1.47 |
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

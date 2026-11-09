# Range-Scalp Bot

*Updated Mon Nov 09 02:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53174 | 46367 | 6807 (85) | 0 | $-14672.30 | -4.4% |
| **+10¢** | 39701 | 31763 | 7938 (110) | 1 | $-13657.95 | -5.5% |
| **+15¢** | 33266 | 24715 | 8551 (141) | 2 | $-12458.70 | -6.0% |
| **+20¢** | 29591 | 20625 | 8966 (186) | 2 | $-10967.54 | -5.9% |
| **+10¢ (15¢ stop)** | 64754 | 64648 | 106 (63) | 0 | $-23977.47 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 02:22 | +10 stop | NEAR | UP | 0.69 | 0.82 | 1.04 |
| 11-09 02:22 | +15 | NEAR | UP | 0.70 | 0.86 | 1.36 |
| 11-09 02:22 | +10 | NEAR | UP | 0.70 | 0.82 | 0.94 |
| 11-09 02:22 | +5 | NEAR | UP | 0.70 | 0.82 | 0.94 |
| 11-09 02:21 | +20 | BNB | UP | 0.69 | 0.95 | 2.35 |
| 11-09 02:21 | +15 | BNB | UP | 0.68 | 0.85 | 1.45 |
| 11-09 02:21 | +10 | BNB | UP | 0.68 | 0.82 | 1.13 |
| 11-09 02:21 | +5 | BNB | UP | 0.68 | 0.74 | 0.30 |
| 11-09 02:21 | +10 stop | SOL | UP | 0.66 | 0.82 | 1.33 |
| 11-09 02:21 | +20 | SOL | UP | 0.66 | 0.94 | 2.56 |
| 11-09 02:21 | +15 | SOL | UP | 0.66 | 0.82 | 1.33 |
| 11-09 02:21 | +10 | SOL | UP | 0.66 | 0.82 | 1.33 |
| 11-09 02:21 | +5 | SOL | UP | 0.67 | 0.73 | 0.30 |
| 11-09 02:18 | +10 stop | DOGE | UP | 0.68 | 0.78 | 0.71 |
| 11-09 02:18 | +10 | DOGE | UP | 0.68 | 0.78 | 0.71 |
| 11-09 02:18 | +5 | DOGE | UP | 0.68 | 0.78 | 0.71 |
| 11-09 02:18 | +5 | HYPE | UP | 0.59 | 0.71 | 0.88 |
| 11-09 02:18 | +10 stop | SOL | UP | 0.59 | 0.77 | 1.50 |
| 11-09 02:18 | +20 | SOL | UP | 0.59 | 0.81 | 1.92 |
| 11-09 02:18 | +15 | SOL | UP | 0.59 | 0.77 | 1.50 |
| 11-09 02:18 | +10 | SOL | UP | 0.59 | 0.77 | 1.50 |
| 11-09 02:18 | +5 | SOL | UP | 0.58 | 0.66 | 0.46 |
| 11-09 02:17 | +10 stop | HYPE | UP | 0.57 | 0.71 | 1.07 |
| 11-09 02:17 | +5 | HYPE | UP | 0.57 | 0.66 | 0.56 |
| 11-09 02:16 | +10 stop | NEAR | UP | 0.70 | 0.81 | 0.82 |
| 11-09 02:16 | +20 | NEAR | UP | 0.70 | 0.91 | 1.83 |
| 11-09 02:16 | +15 | NEAR | UP | 0.70 | 0.86 | 1.34 |
| 11-09 02:16 | +10 | NEAR | UP | 0.70 | 0.81 | 0.82 |
| 11-09 02:16 | +5 | NEAR | UP | 0.70 | 0.81 | 0.82 |
| 11-09 02:16 | +10 stop | HYPE | DOWN | 0.48 | 0.33 | -1.84 |
| 11-09 02:16 | +20 | HYPE | DOWN | 0.48 | open |  |
| 11-09 02:16 | +15 | HYPE | DOWN | 0.48 | open |  |
| 11-09 02:16 | +10 | HYPE | DOWN | 0.48 | open |  |
| 11-09 02:16 | +5 | HYPE | DOWN | 0.48 | 0.53 | 0.14 |
| 11-09 02:16 | +10 stop | DOGE | DOWN | 0.41 | 0.54 | 0.95 |
| 11-09 02:16 | +20 | DOGE | DOWN | 0.41 | open |  |
| 11-09 02:16 | +15 | DOGE | DOWN | 0.41 | open |  |
| 11-09 02:16 | +10 | DOGE | DOWN | 0.41 | 0.54 | 0.95 |
| 11-09 02:16 | +5 | DOGE | DOWN | 0.41 | 0.54 | 0.95 |
| 11-09 02:11 | +10 stop | ZEC | DOWN | 0.57 | 0.77 | 1.69 |

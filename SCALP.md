# Range-Scalp Bot

*Updated Wed Oct 21 15:20 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27353 | 23813 | 3540 (39) | 0 | $-8002.31 | -4.6% |
| **+10¢** | 20567 | 16479 | 4088 (55) | 0 | $-7072.41 | -5.5% |
| **+15¢** | 17225 | 12827 | 4398 (78) | 0 | $-6314.22 | -5.8% |
| **+20¢** | 15248 | 10639 | 4609 (98) | 0 | $-5669.25 | -5.9% |
| **+10¢ (15¢ stop)** | 33561 | 33502 | 59 (32) | 0 | $-12458.40 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 15:18 | +10 stop | DOGE | DOWN | 0.65 | 0.79 | 1.12 |
| 10-21 15:18 | +10 | DOGE | DOWN | 0.65 | 0.79 | 1.12 |
| 10-21 15:17 | +5 | DOGE | DOWN | 0.66 | 0.79 | 1.02 |
| 10-21 15:16 | +5 | XRP | DOWN | 0.64 | 0.72 | 0.48 |
| 10-21 15:16 | +10 stop | NEAR | DOWN | 0.66 | 0.77 | 0.81 |
| 10-21 15:16 | +20 | NEAR | DOWN | 0.66 | 0.90 | 2.18 |
| 10-21 15:16 | +15 | NEAR | DOWN | 0.66 | 0.82 | 1.33 |
| 10-21 15:16 | +10 | NEAR | DOWN | 0.66 | 0.77 | 0.81 |
| 10-21 15:16 | +5 | NEAR | DOWN | 0.66 | 0.74 | 0.50 |
| 10-21 15:16 | +10 stop | XRP | DOWN | 0.60 | 0.72 | 0.88 |
| 10-21 15:16 | +20 | XRP | DOWN | 0.60 | 0.86 | 2.34 |
| 10-21 15:16 | +15 | XRP | DOWN | 0.60 | 0.86 | 2.34 |
| 10-21 15:16 | +10 | XRP | DOWN | 0.60 | 0.72 | 0.88 |
| 10-21 15:16 | +5 | XRP | DOWN | 0.60 | 0.67 | 0.37 |
| 10-21 15:16 | +10 stop | BNB | DOWN | 0.62 | 0.74 | 0.89 |
| 10-21 15:16 | +20 | BNB | DOWN | 0.62 | 0.88 | 2.35 |
| 10-21 15:16 | +15 | BNB | DOWN | 0.62 | 0.77 | 1.20 |
| 10-21 15:16 | +10 | BNB | DOWN | 0.62 | 0.74 | 0.89 |
| 10-21 15:16 | +5 | BNB | DOWN | 0.62 | 0.69 | 0.38 |
| 10-21 15:16 | +10 stop | HYPE | DOWN | 0.66 | 0.78 | 0.91 |
| 10-21 15:16 | +20 | HYPE | DOWN | 0.66 | 0.91 | 2.26 |
| 10-21 15:16 | +15 | HYPE | DOWN | 0.66 | 0.84 | 1.54 |
| 10-21 15:16 | +10 | HYPE | DOWN | 0.66 | 0.78 | 0.91 |
| 10-21 15:16 | +5 | HYPE | DOWN | 0.66 | 0.78 | 0.91 |
| 10-21 15:16 | +10 stop | DOGE | DOWN | 0.58 | 0.69 | 0.77 |
| 10-21 15:16 | +20 | DOGE | DOWN | 0.58 | 0.79 | 1.80 |
| 10-21 15:16 | +15 | DOGE | DOWN | 0.58 | 0.79 | 1.80 |
| 10-21 15:16 | +10 | DOGE | DOWN | 0.58 | 0.69 | 0.77 |
| 10-21 15:16 | +5 | DOGE | DOWN | 0.58 | 0.63 | 0.15 |
| 10-21 15:16 | +10 stop | SOL | DOWN | 0.64 | 0.80 | 1.31 |
| 10-21 15:16 | +20 | SOL | DOWN | 0.64 | 0.87 | 2.05 |
| 10-21 15:16 | +15 | SOL | DOWN | 0.64 | 0.80 | 1.31 |
| 10-21 15:16 | +10 | SOL | DOWN | 0.65 | 0.80 | 1.22 |
| 10-21 15:16 | +5 | SOL | DOWN | 0.65 | 0.80 | 1.22 |
| 10-21 15:10 | +10 stop | XRP | UP | 0.68 | 0.51 | -2.04 |
| 10-21 15:09 | +10 stop | XRP | DOWN | 0.61 | 0.44 | -2.05 |
| 10-21 15:09 | +20 | XRP | DOWN | 0.61 | 0.98 | 3.49 |
| 10-21 15:09 | +15 | XRP | DOWN | 0.61 | 0.98 | 3.49 |
| 10-21 15:09 | +10 | XRP | DOWN | 0.61 | 0.72 | 0.78 |
| 10-21 15:09 | +5 | XRP | DOWN | 0.61 | 0.72 | 0.78 |

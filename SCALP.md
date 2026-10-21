# Range-Scalp Bot

*Updated Wed Oct 21 15:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27373 | 23831 | 3542 (39) | 1 | $-8005.51 | -4.6% |
| **+10¢** | 20584 | 16492 | 4092 (55) | 1 | $-7083.56 | -5.5% |
| **+15¢** | 17239 | 12837 | 4402 (78) | 1 | $-6322.36 | -5.8% |
| **+20¢** | 15260 | 10647 | 4613 (98) | 2 | $-5678.01 | -5.9% |
| **+10¢ (15¢ stop)** | 33579 | 33520 | 59 (32) | 1 | $-12459.97 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 15:40 | +10 stop | HYPE | DOWN | 0.67 | open |  |
| 10-21 15:40 | +10 | HYPE | DOWN | 0.63 | open |  |
| 10-21 15:40 | +5 | HYPE | DOWN | 0.63 | open |  |
| 10-21 15:39 | +10 | HYPE | UP | 0.39 | 0.64 | 2.16 |
| 10-21 15:39 | +5 | HYPE | UP | 0.38 | 0.64 | 2.26 |
| 10-21 15:39 | +10 stop | HYPE | UP | 0.58 | 0.40 | -2.15 |
| 10-21 15:39 | +20 | HYPE | UP | 0.56 | open |  |
| 10-21 15:39 | +15 | HYPE | UP | 0.56 | open |  |
| 10-21 15:39 | +10 | HYPE | UP | 0.55 | 0.65 | 0.66 |
| 10-21 15:39 | +5 | HYPE | UP | 0.58 | 0.65 | 0.36 |
| 10-21 15:38 | +5 | NEAR | UP | 0.63 | 0.68 | 0.17 |
| 10-21 15:38 | +10 stop | NEAR | UP | 0.65 | 0.77 | 0.91 |
| 10-21 15:36 | +10 stop | XRP | UP | 0.70 | 0.83 | 1.05 |
| 10-21 15:36 | +15 | XRP | UP | 0.70 | 0.86 | 1.36 |
| 10-21 15:36 | +10 | XRP | UP | 0.70 | 0.83 | 1.05 |
| 10-21 15:36 | +10 stop | DOGE | UP | 0.70 | 0.86 | 1.36 |
| 10-21 15:36 | +20 | DOGE | UP | 0.70 | open |  |
| 10-21 15:36 | +15 | DOGE | UP | 0.70 | 0.86 | 1.36 |
| 10-21 15:36 | +10 | DOGE | UP | 0.70 | 0.86 | 1.36 |
| 10-21 15:36 | +5 | DOGE | UP | 0.70 | 0.78 | 0.52 |
| 10-21 15:36 | +5 | XRP | UP | 0.71 | 0.83 | 0.95 |
| 10-21 15:32 | +10 stop | XRP | UP | 0.71 | 0.82 | 0.85 |
| 10-21 15:32 | +20 | XRP | UP | 0.69 | 0.89 | 1.78 |
| 10-21 15:32 | +15 | XRP | UP | 0.69 | 0.84 | 1.25 |
| 10-21 15:32 | +10 | XRP | UP | 0.69 | 0.79 | 0.73 |
| 10-21 15:32 | +5 | XRP | UP | 0.69 | 0.79 | 0.73 |
| 10-21 15:32 | +10 stop | BNB | UP | 0.66 | 0.76 | 0.71 |
| 10-21 15:32 | +10 | BNB | UP | 0.66 | 0.76 | 0.71 |
| 10-21 15:32 | +10 stop | DOGE | UP | 0.55 | 0.65 | 0.66 |
| 10-21 15:32 | +20 | DOGE | UP | 0.55 | 0.75 | 1.68 |
| 10-21 15:32 | +15 | DOGE | UP | 0.55 | 0.75 | 1.68 |
| 10-21 15:32 | +10 | DOGE | UP | 0.55 | 0.65 | 0.66 |
| 10-21 15:32 | +5 | DOGE | UP | 0.55 | 0.65 | 0.66 |
| 10-21 15:32 | +5 | BNB | UP | 0.66 | 0.74 | 0.50 |
| 10-21 15:32 | +10 stop | NEAR | UP | 0.55 | 0.34 | -2.43 |
| 10-21 15:32 | +20 | NEAR | UP | 0.55 | 0.77 | 1.90 |
| 10-21 15:32 | +15 | NEAR | UP | 0.55 | 0.77 | 1.90 |
| 10-21 15:32 | +10 | NEAR | UP | 0.55 | 0.68 | 0.97 |
| 10-21 15:32 | +5 | NEAR | UP | 0.55 | 0.62 | 0.36 |
| 10-21 15:31 | +10 stop | BTC | UP | 0.68 | 0.79 | 0.82 |

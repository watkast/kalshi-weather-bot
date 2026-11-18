# Range-Scalp Bot

*Updated Wed Nov 18 00:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63325 | 55235 | 8090 (118) | 5 | $-17262.45 | -4.3% |
| **+10¢** | 47304 | 37837 | 9467 (159) | 4 | $-16159.22 | -5.4% |
| **+15¢** | 39659 | 29451 | 10208 (203) | 5 | $-14638.94 | -5.9% |
| **+20¢** | 35335 | 24623 | 10712 (258) | 5 | $-12880.33 | -5.8% |
| **+10¢ (15¢ stop)** | 77067 | 76909 | 158 (93) | 1 | $-28397.98 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 00:24 | +10 stop | ZEC | UP | 0.65 | open |  |
| 11-18 00:24 | +20 | ZEC | UP | 0.65 | open |  |
| 11-18 00:24 | +15 | ZEC | UP | 0.65 | open |  |
| 11-18 00:24 | +10 | ZEC | UP | 0.65 | open |  |
| 11-18 00:24 | +5 | ZEC | UP | 0.65 | open |  |
| 11-18 00:23 | +10 stop | XRP | UP | 0.39 | 0.65 | 2.23 |
| 11-18 00:23 | +20 | XRP | UP | 0.39 | 0.65 | 2.23 |
| 11-18 00:23 | +15 | XRP | UP | 0.35 | 0.65 | 2.68 |
| 11-18 00:23 | +10 | XRP | UP | 0.36 | 0.65 | 2.57 |
| 11-18 00:23 | +5 | XRP | UP | 0.35 | 0.65 | 2.68 |
| 11-18 00:22 | +10 stop | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 11-18 00:22 | +10 stop | BNB | UP | 0.49 | 0.23 | -2.91 |
| 11-18 00:22 | +5 | BNB | UP | 0.49 | open |  |
| 11-18 00:22 | +5 | HYPE | UP | 0.61 | open |  |
| 11-18 00:20 | +10 stop | HYPE | UP | 0.70 | 0.48 | -2.53 |
| 11-18 00:20 | +15 | HYPE | UP | 0.70 | open |  |
| 11-18 00:20 | +10 | HYPE | UP | 0.70 | open |  |
| 11-18 00:20 | +5 | HYPE | UP | 0.70 | 0.76 | 0.32 |
| 11-18 00:20 | +10 stop | DOGE | UP | 0.57 | 0.67 | 0.66 |
| 11-18 00:19 | +10 stop | BTC | UP | 0.62 | 0.45 | -2.05 |
| 11-18 00:19 | +5 | BNB | UP | 0.59 | 0.71 | 0.88 |
| 11-18 00:19 | +5 | ZEC | UP | 0.71 | 0.76 | 0.22 |
| 11-18 00:18 | +5 | SOL | UP | 0.69 | 0.80 | 0.83 |
| 11-18 00:18 | +5 | BNB | UP | 0.52 | 0.61 | 0.55 |
| 11-18 00:18 | +10 stop | NEAR | UP | 0.63 | 0.77 | 1.10 |
| 11-18 00:18 | +10 | NEAR | UP | 0.63 | 0.77 | 1.10 |
| 11-18 00:18 | +5 | NEAR | UP | 0.63 | 0.77 | 1.10 |
| 11-18 00:18 | +5 | BNB | DOWN | 0.48 | 0.54 | 0.24 |
| 11-18 00:18 | +10 stop | DOGE | DOWN | 0.53 | 0.38 | -1.85 |
| 11-18 00:18 | +20 | DOGE | DOWN | 0.53 | 0.83 | 2.72 |
| 11-18 00:18 | +15 | DOGE | DOWN | 0.53 | 0.83 | 2.72 |
| 11-18 00:18 | +10 | DOGE | DOWN | 0.53 | 0.83 | 2.72 |
| 11-18 00:18 | +5 | DOGE | DOWN | 0.53 | 0.60 | 0.35 |
| 11-18 00:17 | +5 | SOL | UP | 0.59 | 0.66 | 0.37 |
| 11-18 00:17 | +5 | HYPE | UP | 0.71 | 0.76 | 0.22 |
| 11-18 00:17 | +5 | BNB | DOWN | 0.46 | 0.54 | 0.43 |
| 11-18 00:16 | +5 | ZEC | UP | 0.67 | 0.74 | 0.40 |
| 11-18 00:16 | +10 stop | SOL | UP | 0.58 | 0.68 | 0.66 |
| 11-18 00:16 | +20 | SOL | UP | 0.58 | 0.80 | 1.90 |
| 11-18 00:16 | +15 | SOL | UP | 0.58 | 0.73 | 1.18 |

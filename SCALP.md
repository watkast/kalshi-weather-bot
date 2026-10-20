# Range-Scalp Bot

*Updated Tue Oct 20 18:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 26022 | 22665 | 3357 (32) | 3 | $-7580.68 | -4.6% |
| **+10¢** | 19583 | 15702 | 3881 (47) | 4 | $-6715.68 | -5.5% |
| **+15¢** | 16393 | 12217 | 4176 (71) | 5 | $-5989.98 | -5.8% |
| **+20¢** | 14505 | 10128 | 4377 (90) | 5 | $-5372.63 | -5.9% |
| **+10¢ (15¢ stop)** | 31912 | 31859 | 53 (30) | 0 | $-11743.61 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 18:23 | +5 | NEAR | DOWN | 0.52 | 0.59 | 0.35 |
| 10-20 18:22 | +5 | NEAR | DOWN | 0.61 | 0.66 | 0.17 |
| 10-20 18:22 | +10 | HYPE | DOWN | 0.61 | 0.81 | 1.72 |
| 10-20 18:22 | +10 stop | BNB | DOWN | 0.59 | 0.88 | 2.65 |
| 10-20 18:22 | +5 | NEAR | DOWN | 0.62 | 0.67 | 0.17 |
| 10-20 18:21 | +10 stop | BNB | DOWN | 0.62 | 0.45 | -2.05 |
| 10-20 18:20 | +5 | HYPE | DOWN | 0.67 | 0.81 | 1.09 |
| 10-20 18:20 | +10 stop | SOL | DOWN | 0.63 | 0.77 | 1.10 |
| 10-20 18:20 | +10 stop | NEAR | DOWN | 0.59 | 0.73 | 1.09 |
| 10-20 18:20 | +10 | NEAR | DOWN | 0.59 | 0.73 | 1.09 |
| 10-20 18:20 | +5 | NEAR | DOWN | 0.61 | 0.67 | 0.27 |
| 10-20 18:20 | +5 | ETH | DOWN | 0.61 | 0.72 | 0.78 |
| 10-20 18:20 | +5 | HYPE | DOWN | 0.60 | 0.66 | 0.27 |
| 10-20 18:18 | +10 stop | ZEC | DOWN | 0.65 | 0.77 | 0.91 |
| 10-20 18:18 | +10 | ZEC | DOWN | 0.64 | 0.77 | 1.00 |
| 10-20 18:18 | +5 | ZEC | DOWN | 0.64 | 0.73 | 0.59 |
| 10-20 18:18 | +5 | DOGE | DOWN | 0.66 | 0.74 | 0.50 |
| 10-20 18:18 | +10 stop | ETH | DOWN | 0.56 | 0.72 | 1.27 |
| 10-20 18:18 | +10 | ETH | DOWN | 0.57 | 0.72 | 1.17 |
| 10-20 18:18 | +5 | ETH | DOWN | 0.57 | 0.65 | 0.46 |
| 10-20 18:18 | +10 stop | BTC | DOWN | 0.62 | 0.76 | 1.10 |
| 10-20 18:18 | +10 stop | SOL | DOWN | 0.48 | 0.60 | 0.85 |
| 10-20 18:17 | +5 | XRP | DOWN | 0.63 | 0.70 | 0.38 |
| 10-20 18:17 | +10 stop | NEAR | DOWN | 0.61 | 0.73 | 0.89 |
| 10-20 18:17 | +20 | NEAR | DOWN | 0.61 | 0.95 | 3.15 |
| 10-20 18:17 | +15 | NEAR | DOWN | 0.61 | 0.95 | 3.15 |
| 10-20 18:17 | +10 | NEAR | DOWN | 0.61 | 0.73 | 0.89 |
| 10-20 18:17 | +5 | NEAR | DOWN | 0.61 | 0.73 | 0.89 |
| 10-20 18:16 | +10 stop | BTC | UP | 0.55 | 0.35 | -2.34 |
| 10-20 18:16 | +20 | BTC | UP | 0.55 | open |  |
| 10-20 18:16 | +15 | BTC | UP | 0.55 | open |  |
| 10-20 18:16 | +10 | BTC | UP | 0.55 | open |  |
| 10-20 18:16 | +5 | BTC | UP | 0.55 | open |  |
| 10-20 18:16 | +10 stop | BNB | UP | 0.52 | 0.36 | -1.95 |
| 10-20 18:16 | +20 | BNB | UP | 0.52 | open |  |
| 10-20 18:16 | +15 | BNB | UP | 0.52 | open |  |
| 10-20 18:16 | +10 | BNB | UP | 0.52 | open |  |
| 10-20 18:16 | +5 | BNB | UP | 0.52 | open |  |
| 10-20 18:16 | +10 stop | DOGE | DOWN | 0.62 | 0.74 | 0.89 |
| 10-20 18:16 | +20 | DOGE | DOWN | 0.62 | 0.83 | 1.83 |

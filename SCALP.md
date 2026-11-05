# Range-Scalp Bot

*Updated Thu Nov 05 00:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47734 | 41562 | 6172 (73) | 4 | $-13786.32 | -4.6% |
| **+10¢** | 35669 | 28509 | 7160 (98) | 4 | $-12599.69 | -5.6% |
| **+15¢** | 29886 | 22176 | 7710 (126) | 5 | $-11534.52 | -6.1% |
| **+20¢** | 26558 | 18483 | 8075 (166) | 5 | $-10169.75 | -6.1% |
| **+10¢ (15¢ stop)** | 58202 | 58109 | 93 (56) | 0 | $-21635.94 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 00:26 | +10 stop | BTC | UP | 0.63 | 0.40 | -2.64 |
| 11-05 00:26 | +10 stop | XRP | UP | 0.55 | 0.40 | -1.85 |
| 11-05 00:25 | +10 stop | NEAR | UP | 0.69 | 0.47 | -2.53 |
| 11-05 00:25 | +20 | NEAR | UP | 0.69 | open |  |
| 11-05 00:25 | +15 | NEAR | UP | 0.69 | open |  |
| 11-05 00:25 | +10 stop | BTC | UP | 0.50 | 0.73 | 1.98 |
| 11-05 00:24 | +5 | XRP | UP | 0.62 | open |  |
| 11-05 00:24 | +10 stop | XRP | UP | 0.62 | 0.38 | -2.74 |
| 11-05 00:24 | +10 stop | ETH | UP | 0.65 | 0.39 | -2.93 |
| 11-05 00:24 | +5 | XRP | UP | 0.60 | 0.65 | 0.17 |
| 11-05 00:23 | +10 stop | DOGE | UP | 0.60 | 0.32 | -3.13 |
| 11-05 00:23 | +5 | DOGE | UP | 0.60 | open |  |
| 11-05 00:23 | +10 stop | BTC | UP | 0.68 | 0.52 | -1.94 |
| 11-05 00:23 | +10 stop | XRP | UP | 0.52 | 0.65 | 0.96 |
| 11-05 00:23 | +5 | XRP | UP | 0.52 | 0.57 | 0.14 |
| 11-05 00:22 | +5 | XRP | DOWN | 0.58 | 0.63 | 0.15 |
| 11-05 00:22 | +10 stop | BTC | UP | 0.58 | 0.69 | 0.77 |
| 11-05 00:21 | +10 stop | DOGE | DOWN | 0.60 | 0.39 | -2.44 |
| 11-05 00:19 | +10 stop | BNB | UP | 0.59 | 0.71 | 0.83 |
| 11-05 00:19 | +10 stop | ETH | UP | 0.62 | 0.75 | 0.99 |
| 11-05 00:19 | +10 stop | ZEC | DOWN | 0.62 | 0.72 | 0.68 |
| 11-05 00:19 | +15 | ZEC | DOWN | 0.62 | 0.77 | 1.20 |
| 11-05 00:19 | +10 | ZEC | DOWN | 0.62 | 0.72 | 0.68 |
| 11-05 00:19 | +5 | ZEC | DOWN | 0.62 | 0.69 | 0.38 |
| 11-05 00:19 | +5 | XRP | DOWN | 0.59 | 0.64 | 0.17 |
| 11-05 00:19 | +10 stop | NEAR | UP | 0.70 | 0.81 | 0.84 |
| 11-05 00:19 | +15 | NEAR | UP | 0.70 | 0.86 | 1.36 |
| 11-05 00:19 | +10 | NEAR | UP | 0.70 | 0.81 | 0.84 |
| 11-05 00:19 | +5 | NEAR | UP | 0.70 | 0.81 | 0.84 |
| 11-05 00:19 | +5 | XRP | DOWN | 0.56 | 0.66 | 0.66 |
| 11-05 00:18 | +5 | ETH | DOWN | 0.61 | 0.74 | 0.99 |
| 11-05 00:18 | +10 stop | BTC | DOWN | 0.67 | 0.47 | -2.34 |
| 11-05 00:18 | +20 | BTC | DOWN | 0.67 | open |  |
| 11-05 00:18 | +15 | BTC | DOWN | 0.67 | open |  |
| 11-05 00:18 | +10 | BTC | DOWN | 0.67 | open |  |
| 11-05 00:18 | +5 | BTC | DOWN | 0.67 | open |  |
| 11-05 00:18 | +10 stop | HYPE | UP | 0.64 | 0.77 | 1.00 |
| 11-05 00:18 | +20 | HYPE | UP | 0.64 | 0.84 | 1.73 |
| 11-05 00:18 | +15 | HYPE | UP | 0.64 | 0.84 | 1.73 |
| 11-05 00:18 | +10 | HYPE | UP | 0.64 | 0.77 | 1.04 |

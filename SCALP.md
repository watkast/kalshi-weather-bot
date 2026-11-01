# Range-Scalp Bot

*Updated Sun Nov 01 10:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43480 | 37892 | 5588 (63) | 6 | $-12395.94 | -4.5% |
| **+10¢** | 32437 | 25984 | 6453 (85) | 7 | $-11085.97 | -5.4% |
| **+15¢** | 27146 | 20195 | 6951 (112) | 7 | $-10128.83 | -5.9% |
| **+20¢** | 24107 | 16827 | 7280 (146) | 7 | $-8925.74 | -5.9% |
| **+10¢ (15¢ stop)** | 53040 | 52955 | 85 (50) | 3 | $-20051.59 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 10:25 | +10 stop | DOGE | UP | 0.62 | open |  |
| 11-01 10:25 | +10 | DOGE | UP | 0.62 | open |  |
| 11-01 10:25 | +5 | DOGE | UP | 0.62 | open |  |
| 11-01 10:25 | +10 stop | ETH | UP | 0.62 | open |  |
| 11-01 10:24 | +10 stop | ZEC | UP | 0.64 | 0.40 | -2.74 |
| 11-01 10:24 | +5 | HYPE | DOWN | 0.67 | 0.72 | 0.19 |
| 11-01 10:23 | +10 stop | ETH | UP | 0.58 | 0.72 | 1.07 |
| 11-01 10:23 | +10 stop | HYPE | DOWN | 0.62 | 0.80 | 1.47 |
| 11-01 10:23 | +15 | HYPE | DOWN | 0.62 | 0.80 | 1.47 |
| 11-01 10:23 | +10 | HYPE | DOWN | 0.62 | 0.80 | 1.47 |
| 11-01 10:23 | +5 | HYPE | DOWN | 0.62 | 0.68 | 0.23 |
| 11-01 10:21 | +10 stop | BNB | UP | 0.62 | open |  |
| 11-01 10:20 | +10 stop | BTC | DOWN | 0.54 | 0.82 | 2.51 |
| 11-01 10:19 | +10 stop | NEAR | UP | 0.66 | 0.76 | 0.71 |
| 11-01 10:19 | +10 stop | ETH | UP | 0.69 | 0.81 | 0.94 |
| 11-01 10:19 | +5 | NEAR | UP | 0.66 | 0.76 | 0.71 |
| 11-01 10:19 | +10 stop | DOGE | DOWN | 0.38 | 0.54 | 1.25 |
| 11-01 10:19 | +10 | DOGE | DOWN | 0.38 | 0.54 | 1.25 |
| 11-01 10:19 | +5 | DOGE | DOWN | 0.39 | 0.54 | 1.15 |
| 11-01 10:19 | +5 | NEAR | DOWN | 0.55 | 0.66 | 0.76 |
| 11-01 10:18 | +5 | XRP | DOWN | 0.54 | open |  |
| 11-01 10:18 | +10 stop | NEAR | DOWN | 0.62 | 0.38 | -2.74 |
| 11-01 10:18 | +20 | NEAR | DOWN | 0.62 | open |  |
| 11-01 10:18 | +15 | NEAR | DOWN | 0.62 | open |  |
| 11-01 10:18 | +10 | NEAR | DOWN | 0.62 | open |  |
| 11-01 10:18 | +5 | NEAR | DOWN | 0.62 | 0.67 | 0.17 |
| 11-01 10:18 | +10 stop | ZEC | DOWN | 0.67 | 0.41 | -2.93 |
| 11-01 10:18 | +20 | ZEC | DOWN | 0.67 | open |  |
| 11-01 10:18 | +15 | ZEC | DOWN | 0.67 | open |  |
| 11-01 10:18 | +10 | ZEC | DOWN | 0.67 | open |  |
| 11-01 10:18 | +5 | ZEC | DOWN | 0.68 | open |  |
| 11-01 10:18 | +10 stop | XRP | DOWN | 0.54 | 0.25 | -3.22 |
| 11-01 10:18 | +20 | XRP | DOWN | 0.54 | open |  |
| 11-01 10:18 | +15 | XRP | DOWN | 0.54 | open |  |
| 11-01 10:18 | +10 | XRP | DOWN | 0.54 | open |  |
| 11-01 10:18 | +5 | XRP | DOWN | 0.54 | 0.60 | 0.25 |
| 11-01 10:18 | +10 stop | BTC | DOWN | 0.71 | 0.53 | -2.13 |
| 11-01 10:18 | +20 | BTC | DOWN | 0.71 | 0.92 | 1.90 |
| 11-01 10:18 | +15 | BTC | DOWN | 0.71 | 0.86 | 1.26 |
| 11-01 10:18 | +10 | BTC | DOWN | 0.71 | 0.82 | 0.84 |

# Range-Scalp Bot

*Updated Mon Oct 19 09:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 23792 | 20687 | 3105 (31) | 2 | $-7092.90 | -4.7% |
| **+10¢** | 17896 | 14319 | 3577 (45) | 5 | $-6318.02 | -5.6% |
| **+15¢** | 14991 | 11140 | 3851 (67) | 5 | $-5716.49 | -6.1% |
| **+20¢** | 13273 | 9245 | 4028 (86) | 5 | $-5064.65 | -6.1% |
| **+10¢ (15¢ stop)** | 29276 | 29225 | 51 (30) | 1 | $-11064.78 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 09:20 | +10 stop | NEAR | UP | 0.71 | open |  |
| 10-19 09:19 | +10 stop | XRP | UP | 0.71 | 0.81 | 0.74 |
| 10-19 09:19 | +5 | BTC | UP | 0.71 | 0.77 | 0.32 |
| 10-19 09:18 | +10 stop | NEAR | UP | 0.52 | 0.68 | 1.26 |
| 10-19 09:18 | +10 stop | BTC | UP | 0.64 | 0.77 | 1.00 |
| 10-19 09:17 | +5 | XRP | UP | 0.71 | 0.81 | 0.74 |
| 10-19 09:17 | +5 | BTC | UP | 0.62 | 0.71 | 0.58 |
| 10-19 09:17 | +5 | ZEC | UP | 0.67 | 0.73 | 0.30 |
| 10-19 09:17 | +10 stop | ETH | UP | 0.68 | 0.79 | 0.82 |
| 10-19 09:17 | +20 | ETH | UP | 0.68 | 0.88 | 1.76 |
| 10-19 09:17 | +15 | ETH | UP | 0.68 | 0.86 | 1.55 |
| 10-19 09:17 | +10 | ETH | UP | 0.68 | 0.79 | 0.82 |
| 10-19 09:17 | +5 | ETH | UP | 0.68 | 0.79 | 0.82 |
| 10-19 09:17 | +5 | ZEC | DOWN | 0.48 | 0.54 | 0.24 |
| 10-19 09:16 | +10 stop | XRP | DOWN | 0.49 | 0.34 | -1.84 |
| 10-19 09:16 | +20 | XRP | DOWN | 0.49 | open |  |
| 10-19 09:16 | +15 | XRP | DOWN | 0.49 | open |  |
| 10-19 09:16 | +10 | XRP | DOWN | 0.49 | open |  |
| 10-19 09:16 | +5 | XRP | DOWN | 0.49 | 0.54 | 0.14 |
| 10-19 09:16 | +5 | BTC | DOWN | 0.50 | 0.57 | 0.34 |
| 10-19 09:16 | +10 stop | DOGE | DOWN | 0.55 | 0.38 | -2.03 |
| 10-19 09:16 | +20 | DOGE | DOWN | 0.55 | open |  |
| 10-19 09:16 | +15 | DOGE | DOWN | 0.55 | open |  |
| 10-19 09:16 | +10 | DOGE | DOWN | 0.55 | open |  |
| 10-19 09:16 | +5 | DOGE | DOWN | 0.55 | open |  |
| 10-19 09:16 | +10 stop | BTC | DOWN | 0.52 | 0.36 | -1.95 |
| 10-19 09:16 | +20 | BTC | DOWN | 0.52 | open |  |
| 10-19 09:16 | +15 | BTC | DOWN | 0.52 | open |  |
| 10-19 09:16 | +10 | BTC | DOWN | 0.52 | open |  |
| 10-19 09:16 | +5 | BTC | DOWN | 0.52 | 0.57 | 0.14 |
| 10-19 09:16 | +10 stop | ZEC | DOWN | 0.54 | 0.26 | -3.12 |
| 10-19 09:16 | +20 | ZEC | DOWN | 0.54 | open |  |
| 10-19 09:16 | +15 | ZEC | DOWN | 0.55 | open |  |
| 10-19 09:16 | +10 | ZEC | DOWN | 0.55 | open |  |
| 10-19 09:16 | +5 | ZEC | DOWN | 0.54 | 0.61 | 0.35 |
| 10-19 09:16 | +10 stop | NEAR | DOWN | 0.62 | 0.42 | -2.35 |
| 10-19 09:16 | +20 | NEAR | DOWN | 0.62 | open |  |
| 10-19 09:16 | +15 | NEAR | DOWN | 0.62 | open |  |
| 10-19 09:16 | +10 | NEAR | DOWN | 0.62 | open |  |
| 10-19 09:16 | +5 | NEAR | DOWN | 0.62 | open |  |

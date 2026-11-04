# Range-Scalp Bot

*Updated Wed Nov 04 20:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47507 | 41366 | 6141 (73) | 3 | $-13701.25 | -4.6% |
| **+10¢** | 35494 | 28370 | 7124 (98) | 4 | $-12527.02 | -5.6% |
| **+15¢** | 29729 | 22057 | 7672 (126) | 5 | $-11489.81 | -6.2% |
| **+20¢** | 26412 | 18377 | 8035 (166) | 6 | $-10148.80 | -6.1% |
| **+10¢ (15¢ stop)** | 57910 | 57817 | 93 (56) | 0 | $-21593.81 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 20:40 | +10 stop | SOL | DOWN | 0.68 | 0.51 | -2.04 |
| 11-04 20:40 | +10 stop | NEAR | UP | 0.64 | 0.78 | 1.10 |
| 11-04 20:40 | +5 | ETH | UP | 0.65 | 0.74 | 0.60 |
| 11-04 20:39 | +10 stop | NEAR | DOWN | 0.64 | 0.42 | -2.55 |
| 11-04 20:39 | +10 stop | BTC | DOWN | 0.70 | 0.50 | -2.33 |
| 11-04 20:39 | +10 stop | XRP | DOWN | 0.68 | 0.47 | -2.39 |
| 11-04 20:39 | +10 stop | ETH | UP | 0.53 | 0.74 | 1.78 |
| 11-04 20:39 | +20 | ETH | UP | 0.53 | 0.74 | 1.78 |
| 11-04 20:39 | +15 | ETH | UP | 0.53 | 0.74 | 1.78 |
| 11-04 20:39 | +10 | ETH | UP | 0.53 | 0.74 | 1.78 |
| 11-04 20:39 | +5 | ETH | UP | 0.53 | 0.61 | 0.45 |
| 11-04 20:38 | +10 stop | SOL | UP | 0.55 | 0.30 | -2.83 |
| 11-04 20:38 | +20 | SOL | UP | 0.55 | 0.76 | 1.79 |
| 11-04 20:38 | +15 | SOL | UP | 0.57 | 0.76 | 1.59 |
| 11-04 20:38 | +10 | SOL | UP | 0.57 | 0.76 | 1.59 |
| 11-04 20:38 | +5 | SOL | UP | 0.57 | 0.76 | 1.59 |
| 11-04 20:37 | +10 stop | NEAR | UP | 0.66 | 0.46 | -2.34 |
| 11-04 20:37 | +15 | NEAR | UP | 0.66 | 0.89 | 2.07 |
| 11-04 20:37 | +10 | NEAR | UP | 0.66 | 0.78 | 0.91 |
| 11-04 20:37 | +5 | NEAR | UP | 0.66 | 0.78 | 0.91 |
| 11-04 20:37 | +10 stop | XRP | UP | 0.61 | 0.45 | -1.95 |
| 11-04 20:37 | +15 | XRP | UP | 0.61 | open |  |
| 11-04 20:37 | +10 | XRP | UP | 0.61 | 0.72 | 0.78 |
| 11-04 20:37 | +5 | XRP | UP | 0.61 | 0.72 | 0.78 |
| 11-04 20:37 | +10 stop | HYPE | DOWN | 0.57 | 0.75 | 1.48 |
| 11-04 20:36 | +10 stop | BTC | UP | 0.69 | 0.54 | -1.83 |
| 11-04 20:36 | +15 | BTC | UP | 0.69 | open |  |
| 11-04 20:36 | +10 | BTC | UP | 0.69 | open |  |
| 11-04 20:36 | +5 | BTC | UP | 0.69 | open |  |
| 11-04 20:36 | +10 stop | DOGE | UP | 0.58 | 0.37 | -2.45 |
| 11-04 20:36 | +15 | DOGE | UP | 0.58 | open |  |
| 11-04 20:36 | +10 | DOGE | UP | 0.58 | open |  |
| 11-04 20:36 | +5 | DOGE | UP | 0.58 | 0.64 | 0.25 |
| 11-04 20:36 | +10 stop | ZEC | UP | 0.66 | 0.49 | -2.04 |
| 11-04 20:36 | +20 | ZEC | UP | 0.66 | open |  |
| 11-04 20:36 | +15 | ZEC | UP | 0.66 | open |  |
| 11-04 20:36 | +10 | ZEC | UP | 0.66 | open |  |
| 11-04 20:36 | +5 | ZEC | UP | 0.66 | open |  |
| 11-04 20:32 | +10 stop | HYPE | UP | 0.57 | 0.41 | -1.95 |
| 11-04 20:32 | +20 | HYPE | UP | 0.57 | open |  |

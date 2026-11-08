# Range-Scalp Bot

*Updated Sun Nov 08 18:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 52601 | 45856 | 6745 (83) | 5 | $-14602.37 | -4.4% |
| **+10¢** | 39270 | 31410 | 7860 (108) | 5 | $-13585.33 | -5.5% |
| **+15¢** | 32900 | 24429 | 8471 (139) | 5 | $-12439.67 | -6.0% |
| **+20¢** | 29264 | 20386 | 8878 (183) | 7 | $-10946.82 | -6.0% |
| **+10¢ (15¢ stop)** | 64082 | 63976 | 106 (63) | 0 | $-23749.17 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 17:58 | +10 stop | NEAR | UP | 0.52 | 0.66 | 1.06 |
| 11-08 17:56 | +10 stop | BTC | UP | 0.69 | 0.80 | 0.83 |
| 11-08 17:56 | +15 | BTC | UP | 0.69 | 0.95 | 2.37 |
| 11-08 17:56 | +10 | BTC | UP | 0.69 | 0.80 | 0.83 |
| 11-08 17:56 | +5 | BTC | UP | 0.69 | 0.78 | 0.62 |
| 11-08 17:54 | +10 stop | BTC | UP | 0.63 | 0.76 | 1.00 |
| 11-08 17:54 | +20 | BTC | UP | 0.63 | 0.95 | 2.95 |
| 11-08 17:54 | +15 | BTC | UP | 0.63 | 0.78 | 1.20 |
| 11-08 17:54 | +10 | BTC | UP | 0.64 | 0.76 | 0.90 |
| 11-08 17:54 | +5 | BTC | UP | 0.64 | 0.69 | 0.18 |
| 11-08 17:53 | +10 stop | XRP | UP | 0.70 | 0.27 | -4.59 |
| 11-08 17:53 | +10 stop | ETH | UP | 0.71 | 0.81 | 0.74 |
| 11-08 17:52 | +10 stop | XRP | UP | 0.47 | 0.63 | 1.25 |
| 11-08 17:51 | +10 stop | BNB | UP | 0.55 | 0.71 | 1.27 |
| 11-08 17:51 | +10 stop | BTC | UP | 0.70 | 0.83 | 1.05 |
| 11-08 17:51 | +10 | BTC | UP | 0.70 | 0.83 | 1.05 |
| 11-08 17:51 | +5 | BTC | UP | 0.70 | 0.83 | 1.05 |
| 11-08 17:51 | +10 stop | SOL | DOWN | 0.71 | 0.40 | -3.42 |
| 11-08 17:51 | +15 | SOL | DOWN | 0.71 | open |  |
| 11-08 17:51 | +10 | SOL | DOWN | 0.71 | open |  |
| 11-08 17:51 | +5 | SOL | DOWN | 0.71 | open |  |
| 11-08 17:50 | +5 | NEAR | DOWN | 0.68 | 0.74 | 0.30 |
| 11-08 17:50 | +5 | ZEC | UP | 0.59 | 0.70 | 0.78 |
| 11-08 17:50 | +10 stop | HYPE | UP | 0.56 | 0.66 | 0.66 |
| 11-08 17:50 | +10 stop | DOGE | DOWN | 0.69 | 0.52 | -2.03 |
| 11-08 17:50 | +15 | DOGE | DOWN | 0.69 | open |  |
| 11-08 17:50 | +10 | DOGE | DOWN | 0.69 | open |  |
| 11-08 17:50 | +5 | DOGE | DOWN | 0.69 | open |  |
| 11-08 17:50 | +10 stop | ZEC | UP | 0.59 | 0.70 | 0.78 |
| 11-08 17:50 | +20 | ZEC | UP | 0.59 | 0.84 | 2.23 |
| 11-08 17:50 | +15 | ZEC | UP | 0.59 | 0.84 | 2.18 |
| 11-08 17:50 | +10 | ZEC | UP | 0.59 | 0.70 | 0.73 |
| 11-08 17:50 | +5 | ZEC | UP | 0.59 | 0.68 | 0.57 |
| 11-08 17:49 | +10 stop | ETH | UP | 0.58 | 0.68 | 0.66 |
| 11-08 17:48 | +10 stop | XRP | DOWN | 0.71 | 0.43 | -3.10 |
| 11-08 17:48 | +20 | XRP | DOWN | 0.71 | open |  |
| 11-08 17:48 | +15 | XRP | DOWN | 0.71 | 0.88 | 1.50 |
| 11-08 17:48 | +10 | XRP | DOWN | 0.71 | 0.85 | 1.19 |
| 11-08 17:48 | +5 | XRP | DOWN | 0.71 | 0.79 | 0.56 |
| 11-08 17:48 | +10 stop | HYPE | DOWN | 0.58 | 0.41 | -2.05 |

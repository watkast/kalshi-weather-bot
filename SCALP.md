# Range-Scalp Bot

*Updated Thu Nov 05 02:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47887 | 41698 | 6189 (73) | 2 | $-13812.42 | -4.6% |
| **+10¢** | 35780 | 28597 | 7183 (99) | 3 | $-12636.36 | -5.6% |
| **+15¢** | 29979 | 22244 | 7735 (127) | 2 | $-11571.52 | -6.2% |
| **+20¢** | 26636 | 18536 | 8100 (166) | 1 | $-10203.94 | -6.1% |
| **+10¢ (15¢ stop)** | 58395 | 58302 | 93 (56) | 0 | $-21722.48 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 02:27 | +10 stop | ETH | DOWN | 0.61 | 0.74 | 0.99 |
| 11-05 02:27 | +5 | ETH | DOWN | 0.61 | 0.74 | 0.99 |
| 11-05 02:27 | +10 | BTC | DOWN | 0.63 | 0.74 | 0.79 |
| 11-05 02:27 | +5 | BTC | DOWN | 0.63 | 0.74 | 0.79 |
| 11-05 02:26 | +10 stop | SOL | UP | 0.71 | 0.55 | -1.93 |
| 11-05 02:26 | +10 stop | BTC | UP | 0.38 | 0.09 | -3.17 |
| 11-05 02:26 | +10 stop | ZEC | DOWN | 0.61 | 0.71 | 0.68 |
| 11-05 02:26 | +5 | ZEC | DOWN | 0.58 | 0.68 | 0.66 |
| 11-05 02:26 | +10 stop | XRP | DOWN | 0.59 | 0.77 | 1.50 |
| 11-05 02:26 | +20 | XRP | DOWN | 0.59 | 0.80 | 1.81 |
| 11-05 02:26 | +15 | XRP | DOWN | 0.59 | 0.77 | 1.50 |
| 11-05 02:26 | +5 | XRP | DOWN | 0.59 | 0.77 | 1.50 |
| 11-05 02:26 | +10 stop | NEAR | DOWN | 0.67 | 0.90 | 2.11 |
| 11-05 02:26 | +15 | NEAR | DOWN | 0.67 | 0.90 | 2.11 |
| 11-05 02:26 | +10 | NEAR | DOWN | 0.67 | 0.90 | 2.11 |
| 11-05 02:26 | +5 | NEAR | DOWN | 0.67 | 0.90 | 2.11 |
| 11-05 02:25 | +10 stop | HYPE | DOWN | 0.66 | 0.43 | -2.64 |
| 11-05 02:25 | +10 | BTC | DOWN | 0.51 | 0.62 | 0.75 |
| 11-05 02:25 | +5 | BTC | DOWN | 0.51 | 0.62 | 0.75 |
| 11-05 02:25 | +10 stop | DOGE | UP | 0.68 | 0.81 | 1.03 |
| 11-05 02:25 | +20 | DOGE | UP | 0.68 | 0.92 | 2.19 |
| 11-05 02:25 | +15 | DOGE | UP | 0.68 | 0.84 | 1.34 |
| 11-05 02:25 | +10 | DOGE | UP | 0.68 | 0.81 | 1.03 |
| 11-05 02:25 | +5 | DOGE | UP | 0.68 | 0.81 | 1.03 |
| 11-05 02:25 | +10 stop | SOL | DOWN | 0.52 | 0.31 | -2.43 |
| 11-05 02:24 | +10 stop | BTC | DOWN | 0.61 | 0.42 | -2.25 |
| 11-05 02:24 | +5 | ETH | DOWN | 0.66 | 0.77 | 0.81 |
| 11-05 02:24 | +10 stop | BNB | UP | 0.56 | 0.29 | -3.07 |
| 11-05 02:24 | +5 | ETH | DOWN | 0.62 | 0.67 | 0.17 |
| 11-05 02:24 | +10 stop | SOL | UP | 0.68 | 0.53 | -1.84 |
| 11-05 02:23 | +10 stop | XRP | UP | 0.64 | 0.43 | -2.45 |
| 11-05 02:23 | +10 | XRP | UP | 0.64 | open |  |
| 11-05 02:23 | +10 stop | HYPE | UP | 0.55 | 0.34 | -2.47 |
| 11-05 02:23 | +15 | HYPE | UP | 0.55 | open |  |
| 11-05 02:23 | +10 | HYPE | UP | 0.55 | open |  |
| 11-05 02:23 | +5 | HYPE | UP | 0.55 | open |  |
| 11-05 02:23 | +5 | ETH | DOWN | 0.54 | 0.61 | 0.35 |
| 11-05 02:23 | +10 stop | ZEC | DOWN | 0.71 | 0.56 | -1.83 |
| 11-05 02:23 | +20 | ZEC | DOWN | 0.71 | 0.98 | 2.53 |
| 11-05 02:23 | +15 | ZEC | DOWN | 0.71 | 0.91 | 1.73 |

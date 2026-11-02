# Range-Scalp Bot

*Updated Mon Nov 02 10:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44700 | 38928 | 5772 (65) | 0 | $-12900.04 | -4.6% |
| **+10¢** | 33366 | 26685 | 6681 (86) | 2 | $-11713.93 | -5.6% |
| **+15¢** | 27921 | 20732 | 7189 (113) | 1 | $-10731.54 | -6.1% |
| **+20¢** | 24810 | 17283 | 7527 (148) | 3 | $-9453.06 | -6.1% |
| **+10¢ (15¢ stop)** | 54543 | 54456 | 87 (51) | 0 | $-20628.02 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 10:27 | +10 | BTC | DOWN | 0.64 | 0.76 | 0.90 |
| 11-02 10:27 | +10 stop | ETH | UP | 0.58 | 0.79 | 1.80 |
| 11-02 10:27 | +10 | ETH | UP | 0.58 | 0.79 | 1.80 |
| 11-02 10:27 | +5 | ETH | UP | 0.58 | 0.79 | 1.80 |
| 11-02 10:26 | +10 stop | SOL | UP | 0.58 | 0.72 | 1.07 |
| 11-02 10:26 | +5 | DOGE | DOWN | 0.65 | 0.73 | 0.50 |
| 11-02 10:26 | +5 | BTC | DOWN | 0.60 | 0.70 | 0.68 |
| 11-02 10:26 | +10 stop | DOGE | DOWN | 0.54 | 0.64 | 0.65 |
| 11-02 10:26 | +15 | DOGE | DOWN | 0.54 | 0.73 | 1.58 |
| 11-02 10:26 | +5 | DOGE | DOWN | 0.54 | 0.62 | 0.45 |
| 11-02 10:26 | +10 stop | BTC | DOWN | 0.55 | 0.70 | 1.17 |
| 11-02 10:25 | +5 | XRP | UP | 0.62 | 0.73 | 0.79 |
| 11-02 10:25 | +10 stop | XRP | UP | 0.63 | 0.73 | 0.69 |
| 11-02 10:25 | +15 | XRP | UP | 0.62 | 0.79 | 1.41 |
| 11-02 10:25 | +10 | XRP | UP | 0.62 | 0.73 | 0.79 |
| 11-02 10:25 | +5 | XRP | UP | 0.61 | 0.68 | 0.37 |
| 11-02 10:25 | +10 stop | ETH | UP | 0.66 | 0.76 | 0.71 |
| 11-02 10:25 | +15 | ETH | UP | 0.66 | 0.98 | 3.00 |
| 11-02 10:25 | +10 | ETH | UP | 0.66 | 0.76 | 0.71 |
| 11-02 10:25 | +5 | ETH | UP | 0.66 | 0.71 | 0.19 |
| 11-02 10:24 | +10 stop | SOL | UP | 0.66 | 0.49 | -2.04 |
| 11-02 10:24 | +10 | SOL | UP | 0.66 | 0.80 | 1.12 |
| 11-02 10:24 | +5 | SOL | UP | 0.66 | 0.72 | 0.29 |
| 11-02 10:24 | +10 stop | BTC | UP | 0.51 | 0.64 | 0.95 |
| 11-02 10:24 | +10 stop | ZEC | DOWN | 0.52 | 0.69 | 1.37 |
| 11-02 10:23 | +10 stop | DOGE | UP | 0.69 | 0.50 | -2.23 |
| 11-02 10:23 | +10 | DOGE | UP | 0.69 | open |  |
| 11-02 10:23 | +5 | DOGE | UP | 0.60 | 0.71 | 0.78 |
| 11-02 10:23 | +10 stop | ZEC | UP | 0.44 | 0.54 | 0.64 |
| 11-02 10:23 | +10 stop | SOL | UP | 0.64 | 0.74 | 0.69 |
| 11-02 10:23 | +10 stop | ZEC | DOWN | 0.45 | 0.59 | 1.05 |
| 11-02 10:22 | +10 stop | ETH | DOWN | 0.41 | 0.59 | 1.46 |
| 11-02 10:22 | +20 | ETH | DOWN | 0.41 | open |  |
| 11-02 10:22 | +10 | ETH | DOWN | 0.41 | 0.59 | 1.46 |
| 11-02 10:22 | +5 | ETH | DOWN | 0.41 | 0.59 | 1.46 |
| 11-02 10:22 | +10 stop | XRP | UP | 0.70 | 0.55 | -1.83 |
| 11-02 10:22 | +20 | XRP | UP | 0.70 | 0.97 | 2.54 |
| 11-02 10:22 | +15 | XRP | UP | 0.70 | 0.86 | 1.36 |
| 11-02 10:22 | +10 | XRP | UP | 0.70 | 0.84 | 1.15 |
| 11-02 10:22 | +5 | XRP | UP | 0.70 | 0.76 | 0.32 |

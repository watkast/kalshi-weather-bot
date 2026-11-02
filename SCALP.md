# Range-Scalp Bot

*Updated Mon Nov 02 06:49 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44554 | 38792 | 5762 (65) | 0 | $-12919.17 | -4.6% |
| **+10¢** | 33255 | 26592 | 6663 (86) | 2 | $-11706.61 | -5.6% |
| **+15¢** | 27838 | 20668 | 7170 (113) | 4 | $-10715.93 | -6.1% |
| **+20¢** | 24741 | 17236 | 7505 (147) | 6 | $-9421.91 | -6.1% |
| **+10¢ (15¢ stop)** | 54386 | 54300 | 86 (51) | 2 | $-20629.93 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 06:47 | +10 stop | DOGE | UP | 0.70 | 0.84 | 1.15 |
| 11-02 06:47 | +20 | DOGE | UP | 0.70 | open |  |
| 11-02 06:47 | +15 | DOGE | UP | 0.71 | 0.89 | 1.58 |
| 11-02 06:47 | +10 | DOGE | UP | 0.71 | 0.84 | 1.05 |
| 11-02 06:47 | +5 | DOGE | UP | 0.70 | 0.75 | 0.21 |
| 11-02 06:46 | +10 stop | BNB | UP | 0.68 | 0.83 | 1.24 |
| 11-02 06:46 | +20 | BNB | UP | 0.68 | open |  |
| 11-02 06:46 | +15 | BNB | UP | 0.68 | 0.83 | 1.24 |
| 11-02 06:46 | +10 | BNB | UP | 0.68 | 0.83 | 1.24 |
| 11-02 06:46 | +5 | BNB | UP | 0.68 | 0.73 | 0.20 |
| 11-02 06:46 | +10 stop | ETH | UP | 0.71 | open |  |
| 11-02 06:46 | +20 | ETH | UP | 0.71 | open |  |
| 11-02 06:46 | +15 | ETH | UP | 0.71 | open |  |
| 11-02 06:46 | +10 | ETH | UP | 0.71 | open |  |
| 11-02 06:46 | +5 | ETH | UP | 0.71 | 0.79 | 0.53 |
| 11-02 06:46 | +10 stop | XRP | UP | 0.69 | 0.80 | 0.83 |
| 11-02 06:46 | +20 | XRP | UP | 0.69 | 0.91 | 1.97 |
| 11-02 06:46 | +15 | XRP | UP | 0.69 | 0.91 | 1.97 |
| 11-02 06:46 | +10 | XRP | UP | 0.68 | 0.80 | 0.92 |
| 11-02 06:46 | +5 | XRP | UP | 0.69 | 0.80 | 0.83 |
| 11-02 06:46 | +10 stop | BTC | UP | 0.64 | 0.77 | 1.00 |
| 11-02 06:46 | +20 | BTC | UP | 0.64 | open |  |
| 11-02 06:46 | +15 | BTC | UP | 0.64 | open |  |
| 11-02 06:46 | +10 | BTC | UP | 0.64 | 0.77 | 1.00 |
| 11-02 06:46 | +5 | BTC | UP | 0.64 | 0.72 | 0.48 |
| 11-02 06:46 | +10 stop | NEAR | UP | 0.66 | open |  |
| 11-02 06:46 | +20 | NEAR | UP | 0.67 | open |  |
| 11-02 06:46 | +15 | NEAR | UP | 0.67 | open |  |
| 11-02 06:46 | +10 | NEAR | UP | 0.67 | open |  |
| 11-02 06:46 | +5 | NEAR | UP | 0.67 | 0.75 | 0.50 |
| 11-02 06:46 | +10 stop | HYPE | UP | 0.67 | 0.80 | 0.98 |
| 11-02 06:46 | +20 | HYPE | UP | 0.67 | open |  |
| 11-02 06:46 | +15 | HYPE | UP | 0.67 | open |  |
| 11-02 06:46 | +10 | HYPE | UP | 0.67 | 0.80 | 0.98 |
| 11-02 06:46 | +5 | HYPE | UP | 0.67 | 0.80 | 0.98 |
| 11-02 06:40 | +10 stop | ZEC | DOWN | 0.70 | 0.88 | 1.57 |
| 11-02 06:39 | +10 stop | SOL | DOWN | 0.67 | 0.80 | 1.02 |
| 11-02 06:39 | +15 | SOL | DOWN | 0.67 | 0.88 | 1.86 |
| 11-02 06:38 | +10 stop | BTC | DOWN | 0.71 | 0.81 | 0.74 |
| 11-02 06:38 | +10 stop | ZEC | UP | 0.50 | 0.35 | -1.84 |

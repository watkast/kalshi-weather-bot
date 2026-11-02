# Range-Scalp Bot

*Updated Mon Nov 02 03:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44288 | 38569 | 5719 (65) | 4 | $-12796.71 | -4.6% |
| **+10¢** | 33056 | 26443 | 6613 (86) | 4 | $-11576.77 | -5.6% |
| **+15¢** | 27668 | 20551 | 7117 (113) | 4 | $-10585.89 | -6.1% |
| **+20¢** | 24587 | 17137 | 7450 (147) | 5 | $-9302.60 | -6.0% |
| **+10¢ (15¢ stop)** | 54038 | 53952 | 86 (51) | 4 | $-20495.70 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 03:05 | +10 stop | ETH | DOWN | 0.58 | open |  |
| 11-02 03:05 | +15 | ETH | DOWN | 0.58 | open |  |
| 11-02 03:05 | +10 stop | SOL | DOWN | 0.64 | open |  |
| 11-02 03:05 | +10 | SOL | DOWN | 0.64 | open |  |
| 11-02 03:05 | +5 | SOL | DOWN | 0.64 | open |  |
| 11-02 03:05 | +10 | BTC | UP | 0.65 | open |  |
| 11-02 03:05 | +5 | BTC | UP | 0.65 | open |  |
| 11-02 03:05 | +20 | BNB | UP | 0.69 | open |  |
| 11-02 03:05 | +15 | BNB | UP | 0.69 | open |  |
| 11-02 03:05 | +5 | BNB | UP | 0.69 | open |  |
| 11-02 03:04 | +10 stop | ETH | UP | 0.65 | 0.46 | -2.24 |
| 11-02 03:04 | +10 stop | BTC | UP | 0.65 | open |  |
| 11-02 03:04 | +5 | BTC | UP | 0.65 | 0.74 | 0.60 |
| 11-02 03:04 | +10 stop | BNB | UP | 0.70 | open |  |
| 11-02 03:04 | +10 | BNB | UP | 0.70 | open |  |
| 11-02 03:03 | +10 stop | XRP | UP | 0.59 | 0.75 | 1.29 |
| 11-02 03:03 | +10 stop | SOL | DOWN | 0.53 | 0.31 | -2.53 |
| 11-02 03:03 | +10 stop | BTC | DOWN | 0.56 | 0.34 | -2.54 |
| 11-02 03:03 | +10 stop | DOGE | UP | 0.67 | 0.83 | 1.34 |
| 11-02 03:03 | +20 | DOGE | UP | 0.67 | 0.87 | 1.76 |
| 11-02 03:03 | +15 | DOGE | UP | 0.67 | 0.83 | 1.34 |
| 11-02 03:03 | +10 | DOGE | UP | 0.67 | 0.83 | 1.34 |
| 11-02 03:03 | +5 | DOGE | UP | 0.67 | 0.83 | 1.34 |
| 11-02 03:03 | +10 | NEAR | UP | 0.59 | 0.73 | 1.09 |
| 11-02 03:03 | +5 | NEAR | UP | 0.59 | 0.66 | 0.37 |
| 11-02 03:02 | +10 stop | XRP | UP | 0.70 | 0.55 | -1.83 |
| 11-02 03:02 | +10 | XRP | UP | 0.70 | 0.87 | 1.47 |
| 11-02 03:02 | +5 | XRP | UP | 0.70 | 0.75 | 0.21 |
| 11-02 03:02 | +10 stop | HYPE | UP | 0.61 | 0.71 | 0.68 |
| 11-02 03:02 | +20 | HYPE | UP | 0.61 | 0.81 | 1.72 |
| 11-02 03:02 | +15 | HYPE | UP | 0.61 | 0.81 | 1.72 |
| 11-02 03:02 | +10 | HYPE | UP | 0.58 | 0.71 | 0.97 |
| 11-02 03:02 | +5 | HYPE | UP | 0.58 | 0.71 | 0.97 |
| 11-02 03:02 | +10 stop | SOL | UP | 0.62 | 0.42 | -2.35 |
| 11-02 03:02 | +20 | SOL | UP | 0.62 | open |  |
| 11-02 03:02 | +15 | SOL | UP | 0.62 | open |  |
| 11-02 03:02 | +10 | SOL | UP | 0.62 | 0.76 | 1.10 |
| 11-02 03:02 | +5 | SOL | UP | 0.62 | 0.68 | 0.27 |
| 11-02 03:02 | +10 stop | NEAR | UP | 0.66 | 0.82 | 1.33 |
| 11-02 03:02 | +20 | NEAR | UP | 0.65 | open |  |

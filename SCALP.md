# Range-Scalp Bot

*Updated Mon Nov 02 03:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44306 | 38587 | 5719 (65) | 6 | $-12787.38 | -4.6% |
| **+10¢** | 33069 | 26455 | 6614 (86) | 6 | $-11570.71 | -5.6% |
| **+15¢** | 27680 | 20562 | 7118 (113) | 6 | $-10576.12 | -6.1% |
| **+20¢** | 24597 | 17147 | 7450 (147) | 6 | $-9282.42 | -6.0% |
| **+10¢ (15¢ stop)** | 54066 | 53980 | 86 (51) | 0 | $-20505.84 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 03:24 | +10 stop | XRP | DOWN | 0.67 | 0.09 | -6.05 |
| 11-02 03:23 | +5 | XRP | DOWN | 0.70 | open |  |
| 11-02 03:23 | +10 stop | XRP | DOWN | 0.71 | 0.55 | -1.93 |
| 11-02 03:23 | +20 | XRP | DOWN | 0.71 | open |  |
| 11-02 03:23 | +15 | XRP | DOWN | 0.71 | open |  |
| 11-02 03:23 | +10 | XRP | DOWN | 0.71 | open |  |
| 11-02 03:21 | +10 stop | SOL | UP | 0.65 | 0.75 | 0.70 |
| 11-02 03:21 | +10 stop | ETH | UP | 0.70 | 0.89 | 1.68 |
| 11-02 03:21 | +10 stop | BTC | UP | 0.65 | 0.82 | 1.43 |
| 11-02 03:21 | +10 stop | HYPE | DOWN | 0.65 | 0.86 | 1.81 |
| 11-02 03:21 | +10 | HYPE | DOWN | 0.65 | 0.86 | 1.81 |
| 11-02 03:21 | +5 | HYPE | DOWN | 0.65 | 0.86 | 1.81 |
| 11-02 03:21 | +10 stop | ZEC | UP | 0.69 | 0.79 | 0.73 |
| 11-02 03:21 | +10 stop | NEAR | DOWN | 0.41 | 0.62 | 1.76 |
| 11-02 03:20 | +10 stop | BNB | UP | 0.59 | 0.72 | 0.98 |
| 11-02 03:20 | +5 | ZEC | DOWN | 0.65 | open |  |
| 11-02 03:20 | +5 | SOL | DOWN | 0.59 | open |  |
| 11-02 03:20 | +10 stop | ETH | UP | 0.56 | 0.66 | 0.66 |
| 11-02 03:19 | +10 stop | ZEC | DOWN | 0.58 | 0.43 | -1.86 |
| 11-02 03:19 | +15 | ZEC | DOWN | 0.55 | open |  |
| 11-02 03:19 | +10 | ZEC | DOWN | 0.55 | open |  |
| 11-02 03:19 | +5 | ZEC | DOWN | 0.55 | 0.63 | 0.45 |
| 11-02 03:19 | +10 stop | HYPE | DOWN | 0.62 | 0.76 | 1.10 |
| 11-02 03:19 | +15 | HYPE | DOWN | 0.61 | 0.86 | 2.19 |
| 11-02 03:19 | +10 | HYPE | DOWN | 0.61 | 0.76 | 1.15 |
| 11-02 03:19 | +5 | HYPE | DOWN | 0.62 | 0.76 | 1.06 |
| 11-02 03:19 | +10 stop | DOGE | UP | 0.63 | 0.82 | 1.62 |
| 11-02 03:19 | +20 | DOGE | UP | 0.63 | 0.83 | 1.73 |
| 11-02 03:19 | +15 | DOGE | UP | 0.63 | 0.82 | 1.62 |
| 11-02 03:19 | +10 | DOGE | UP | 0.63 | 0.82 | 1.62 |
| 11-02 03:19 | +5 | DOGE | UP | 0.63 | 0.70 | 0.38 |
| 11-02 03:19 | +5 | SOL | DOWN | 0.64 | 0.69 | 0.18 |
| 11-02 03:19 | +10 stop | BNB | DOWN | 0.61 | 0.45 | -1.95 |
| 11-02 03:18 | +5 | SOL | DOWN | 0.62 | 0.67 | 0.17 |
| 11-02 03:18 | +10 stop | BTC | DOWN | 0.51 | 0.36 | -1.85 |
| 11-02 03:18 | +20 | BTC | DOWN | 0.51 | open |  |
| 11-02 03:18 | +15 | BTC | DOWN | 0.51 | open |  |
| 11-02 03:18 | +10 | BTC | DOWN | 0.51 | open |  |
| 11-02 03:18 | +5 | BTC | DOWN | 0.51 | open |  |
| 11-02 03:17 | +10 stop | ETH | DOWN | 0.57 | 0.34 | -2.64 |

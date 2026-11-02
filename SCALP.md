# Range-Scalp Bot

*Updated Mon Nov 02 10:50 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44742 | 38965 | 5777 (65) | 1 | $-12911.92 | -4.6% |
| **+10¢** | 33395 | 26707 | 6688 (86) | 3 | $-11738.80 | -5.6% |
| **+15¢** | 27937 | 20739 | 7198 (113) | 5 | $-10781.26 | -6.1% |
| **+20¢** | 24824 | 17286 | 7538 (148) | 6 | $-9517.00 | -6.1% |
| **+10¢ (15¢ stop)** | 54592 | 54505 | 87 (51) | 0 | $-20639.48 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 10:49 | +10 stop | BNB | UP | 0.54 | 0.35 | -2.24 |
| 11-02 10:48 | +5 | DOGE | UP | 0.64 | 0.73 | 0.59 |
| 11-02 10:48 | +10 stop | BTC | UP | 0.66 | 0.79 | 1.02 |
| 11-02 10:48 | +10 | BTC | UP | 0.66 | 0.79 | 1.02 |
| 11-02 10:48 | +5 | BTC | UP | 0.66 | 0.73 | 0.40 |
| 11-02 10:48 | +10 stop | HYPE | UP | 0.64 | 0.78 | 1.10 |
| 11-02 10:48 | +10 | HYPE | UP | 0.65 | 0.78 | 1.01 |
| 11-02 10:48 | +5 | HYPE | UP | 0.66 | 0.78 | 0.91 |
| 11-02 10:48 | +5 | SOL | UP | 0.59 | 0.70 | 0.78 |
| 11-02 10:47 | +5 | SOL | UP | 0.58 | 0.65 | 0.36 |
| 11-02 10:47 | +10 stop | DOGE | UP | 0.71 | 0.83 | 0.95 |
| 11-02 10:47 | +5 | DOGE | UP | 0.64 | 0.69 | 0.18 |
| 11-02 10:47 | +10 stop | ETH | UP | 0.62 | 0.79 | 1.41 |
| 11-02 10:47 | +10 | ETH | UP | 0.62 | 0.79 | 1.41 |
| 11-02 10:47 | +5 | ETH | UP | 0.62 | 0.79 | 1.41 |
| 11-02 10:47 | +10 stop | HYPE | UP | 0.61 | 0.71 | 0.68 |
| 11-02 10:47 | +20 | HYPE | UP | 0.61 | 0.83 | 1.93 |
| 11-02 10:47 | +15 | HYPE | UP | 0.61 | 0.78 | 1.40 |
| 11-02 10:47 | +10 | HYPE | UP | 0.61 | 0.71 | 0.68 |
| 11-02 10:47 | +5 | HYPE | UP | 0.61 | 0.67 | 0.27 |
| 11-02 10:47 | +10 stop | SOL | UP | 0.61 | 0.80 | 1.61 |
| 11-02 10:47 | +5 | SOL | UP | 0.61 | 0.67 | 0.27 |
| 11-02 10:46 | +10 stop | BTC | UP | 0.60 | 0.72 | 0.88 |
| 11-02 10:46 | +15 | BTC | UP | 0.60 | 0.79 | 1.61 |
| 11-02 10:46 | +10 | BTC | UP | 0.60 | 0.72 | 0.88 |
| 11-02 10:46 | +5 | BTC | UP | 0.60 | 0.66 | 0.27 |
| 11-02 10:46 | +10 stop | XRP | UP | 0.66 | 0.76 | 0.71 |
| 11-02 10:46 | +10 | XRP | UP | 0.66 | 0.76 | 0.71 |
| 11-02 10:46 | +5 | XRP | UP | 0.67 | 0.72 | 0.22 |
| 11-02 10:46 | +10 stop | DOGE | DOWN | 0.52 | 0.37 | -1.85 |
| 11-02 10:46 | +20 | DOGE | DOWN | 0.52 | open |  |
| 11-02 10:46 | +15 | DOGE | DOWN | 0.52 | open |  |
| 11-02 10:46 | +10 | DOGE | DOWN | 0.52 | open |  |
| 11-02 10:46 | +5 | DOGE | DOWN | 0.52 | 0.59 | 0.35 |
| 11-02 10:46 | +10 stop | BTC | DOWN | 0.46 | 0.63 | 1.35 |
| 11-02 10:46 | +20 | BTC | DOWN | 0.47 | open |  |
| 11-02 10:46 | +15 | BTC | DOWN | 0.47 | 0.63 | 1.25 |
| 11-02 10:46 | +10 | BTC | DOWN | 0.47 | 0.63 | 1.25 |
| 11-02 10:46 | +5 | BTC | DOWN | 0.47 | 0.63 | 1.25 |
| 11-02 10:46 | +10 stop | ETH | DOWN | 0.52 | 0.64 | 0.85 |

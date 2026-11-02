# Range-Scalp Bot

*Updated Mon Nov 02 00:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44101 | 38413 | 5688 (65) | 0 | $-12691.71 | -4.6% |
| **+10¢** | 32911 | 26338 | 6573 (86) | 0 | $-11442.16 | -5.5% |
| **+15¢** | 27546 | 20473 | 7073 (113) | 1 | $-10437.02 | -6.0% |
| **+20¢** | 24472 | 17066 | 7406 (147) | 1 | $-9180.01 | -6.0% |
| **+10¢ (15¢ stop)** | 53787 | 53701 | 86 (51) | 0 | $-20336.30 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 00:02 | +5 | HYPE | UP | 0.70 | 0.77 | 0.42 |
| 11-02 00:01 | +10 stop | BTC | UP | 0.64 | 0.75 | 0.79 |
| 11-02 00:01 | +20 | BTC | UP | 0.64 | 0.87 | 2.05 |
| 11-02 00:01 | +15 | BTC | UP | 0.64 | 0.81 | 1.42 |
| 11-02 00:01 | +10 | BTC | UP | 0.65 | 0.75 | 0.70 |
| 11-02 00:01 | +5 | BTC | UP | 0.65 | 0.75 | 0.70 |
| 11-02 00:01 | +10 stop | XRP | UP | 0.71 | 0.82 | 0.84 |
| 11-02 00:01 | +20 | XRP | UP | 0.71 | open |  |
| 11-02 00:01 | +15 | XRP | UP | 0.71 | open |  |
| 11-02 00:01 | +10 | XRP | UP | 0.71 | 0.82 | 0.84 |
| 11-02 00:01 | +5 | XRP | UP | 0.71 | 0.77 | 0.32 |
| 11-02 00:01 | +10 stop | HYPE | UP | 0.62 | 0.77 | 1.20 |
| 11-02 00:01 | +20 | HYPE | UP | 0.62 | 0.82 | 1.72 |
| 11-02 00:01 | +15 | HYPE | UP | 0.62 | 0.77 | 1.20 |
| 11-02 00:01 | +10 | HYPE | UP | 0.62 | 0.77 | 1.20 |
| 11-02 00:01 | +5 | HYPE | UP | 0.62 | 0.70 | 0.48 |
| 11-02 00:01 | +10 stop | BNB | UP | 0.65 | 0.77 | 0.91 |
| 11-02 00:01 | +20 | BNB | UP | 0.66 | 0.87 | 1.89 |
| 11-02 00:01 | +15 | BNB | UP | 0.64 | 0.79 | 1.21 |
| 11-02 00:01 | +10 | BNB | UP | 0.64 | 0.74 | 0.69 |
| 11-02 00:01 | +5 | BNB | UP | 0.64 | 0.71 | 0.38 |
| 11-01 23:58 | +10 stop | DOGE | UP | 0.54 | 0.19 | -3.79 |
| 11-01 23:58 | +5 | DOGE | UP | 0.54 | 0.62 | 0.45 |
| 11-01 23:56 | +10 stop | DOGE | UP | 0.62 | 0.77 | 1.20 |
| 11-01 23:56 | +5 | DOGE | UP | 0.63 | 0.77 | 1.10 |
| 11-01 23:56 | +10 stop | BTC | UP | 0.67 | 0.86 | 1.65 |
| 11-01 23:56 | +10 stop | HYPE | UP | 0.68 | 0.81 | 1.03 |
| 11-01 23:56 | +5 | HYPE | UP | 0.68 | 0.76 | 0.51 |
| 11-01 23:55 | +10 stop | ZEC | DOWN | 0.63 | 0.48 | -1.85 |
| 11-01 23:55 | +20 | ZEC | DOWN | 0.63 | 0.84 | 1.83 |
| 11-01 23:54 | +10 stop | DOGE | DOWN | 0.61 | 0.43 | -2.15 |
| 11-01 23:54 | +10 stop | SOL | UP | 0.64 | 0.77 | 1.00 |
| 11-01 23:54 | +10 stop | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 11-01 23:54 | +10 stop | BTC | DOWN | 0.68 | 0.49 | -2.24 |
| 11-01 23:53 | +10 stop | ETH | UP | 0.61 | 0.77 | 1.30 |
| 11-01 23:52 | +10 stop | ZEC | DOWN | 0.60 | 0.72 | 0.88 |
| 11-01 23:51 | +10 stop | BTC | UP | 0.61 | 0.44 | -2.05 |
| 11-01 23:51 | +10 stop | HYPE | UP | 0.69 | 0.89 | 1.74 |
| 11-01 23:51 | +5 | HYPE | UP | 0.69 | 0.75 | 0.27 |
| 11-01 23:51 | +10 stop | DOGE | UP | 0.71 | 0.42 | -3.23 |

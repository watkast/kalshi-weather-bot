# Range-Scalp Bot

*Updated Mon Nov 02 00:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44135 | 38442 | 5693 (65) | 0 | $-12704.63 | -4.6% |
| **+10¢** | 32938 | 26356 | 6582 (86) | 1 | $-11477.70 | -5.5% |
| **+15¢** | 27569 | 20485 | 7084 (113) | 1 | $-10486.76 | -6.1% |
| **+20¢** | 24495 | 17078 | 7417 (147) | 1 | $-9223.72 | -6.0% |
| **+10¢ (15¢ stop)** | 53825 | 53739 | 86 (51) | 1 | $-20349.13 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 00:45 | +10 stop | HYPE | UP | 0.61 | open |  |
| 11-02 00:45 | +20 | HYPE | UP | 0.61 | open |  |
| 11-02 00:45 | +15 | HYPE | UP | 0.61 | open |  |
| 11-02 00:45 | +10 | HYPE | UP | 0.61 | open |  |
| 11-02 00:45 | +5 | HYPE | UP | 0.61 | 0.69 | 0.48 |
| 11-02 00:42 | +10 stop | XRP | DOWN | 0.47 | 0.22 | -2.81 |
| 11-02 00:42 | +10 | XRP | DOWN | 0.47 | yes | -4.88 |
| 11-02 00:42 | +5 | XRP | DOWN | 0.47 | 0.54 | 0.34 |
| 11-02 00:37 | +20 | XRP | DOWN | 0.62 | yes | -6.37 |
| 11-02 00:36 | +10 stop | HYPE | UP | 0.71 | 0.81 | 0.76 |
| 11-02 00:36 | +5 | HYPE | UP | 0.66 | 0.75 | 0.60 |
| 11-02 00:35 | +10 stop | HYPE | DOWN | 0.68 | 0.35 | -3.62 |
| 11-02 00:34 | +10 stop | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 11-02 00:34 | +15 | XRP | DOWN | 0.71 | yes | -7.25 |
| 11-02 00:34 | +10 | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 11-02 00:34 | +5 | XRP | DOWN | 0.71 | 0.76 | 0.22 |
| 11-02 00:33 | +10 stop | BNB | DOWN | 0.70 | 0.81 | 0.83 |
| 11-02 00:32 | +5 | SOL | DOWN | 0.66 | 0.79 | 1.02 |
| 11-02 00:32 | +10 stop | NEAR | DOWN | 0.53 | 0.76 | 1.99 |
| 11-02 00:32 | +10 stop | DOGE | DOWN | 0.71 | 0.83 | 0.95 |
| 11-02 00:32 | +20 | DOGE | DOWN | 0.71 | 0.92 | 1.85 |
| 11-02 00:32 | +15 | DOGE | DOWN | 0.71 | 0.86 | 1.26 |
| 11-02 00:32 | +10 | DOGE | DOWN | 0.71 | 0.83 | 0.95 |
| 11-02 00:32 | +5 | DOGE | DOWN | 0.71 | 0.76 | 0.22 |
| 11-02 00:32 | +10 stop | SOL | DOWN | 0.59 | 0.79 | 1.71 |
| 11-02 00:32 | +20 | SOL | DOWN | 0.59 | 0.79 | 1.71 |
| 11-02 00:32 | +15 | SOL | DOWN | 0.59 | 0.79 | 1.71 |
| 11-02 00:32 | +10 | SOL | DOWN | 0.58 | 0.79 | 1.80 |
| 11-02 00:32 | +5 | SOL | DOWN | 0.58 | 0.64 | 0.25 |
| 11-02 00:31 | +10 stop | HYPE | UP | 0.66 | 0.47 | -2.24 |
| 11-02 00:31 | +10 stop | BNB | DOWN | 0.57 | 0.67 | 0.66 |
| 11-02 00:31 | +10 stop | XRP | DOWN | 0.53 | 0.71 | 1.47 |
| 11-02 00:31 | +20 | XRP | DOWN | 0.53 | 0.75 | 1.88 |
| 11-02 00:31 | +15 | XRP | DOWN | 0.53 | 0.71 | 1.47 |
| 11-02 00:31 | +10 | XRP | DOWN | 0.53 | 0.71 | 1.47 |
| 11-02 00:31 | +5 | XRP | DOWN | 0.53 | 0.71 | 1.47 |
| 11-02 00:31 | +10 stop | NEAR | DOWN | 0.69 | 0.50 | -2.23 |
| 11-02 00:31 | +20 | NEAR | DOWN | 0.69 | 0.93 | 2.18 |
| 11-02 00:31 | +15 | NEAR | DOWN | 0.69 | 0.85 | 1.36 |
| 11-02 00:31 | +10 | NEAR | DOWN | 0.69 | 0.85 | 1.36 |

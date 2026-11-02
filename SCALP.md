# Range-Scalp Bot

*Updated Mon Nov 02 04:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44414 | 38672 | 5742 (65) | 4 | $-12874.96 | -4.6% |
| **+10¢** | 33152 | 26513 | 6639 (86) | 5 | $-11655.58 | -5.6% |
| **+15¢** | 27752 | 20607 | 7145 (113) | 5 | $-10665.14 | -6.1% |
| **+20¢** | 24664 | 17187 | 7477 (147) | 5 | $-9359.61 | -6.0% |
| **+10¢ (15¢ stop)** | 54211 | 54125 | 86 (51) | 0 | $-20592.83 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 04:56 | +10 stop | DOGE | DOWN | 0.70 | 0.82 | 0.94 |
| 11-02 04:52 | +10 stop | ZEC | DOWN | 0.64 | 0.46 | -2.15 |
| 11-02 04:50 | +10 stop | BTC | DOWN | 0.71 | 0.84 | 1.05 |
| 11-02 04:50 | +5 | BTC | DOWN | 0.69 | 0.74 | 0.21 |
| 11-02 04:50 | +10 stop | BNB | DOWN | 0.71 | 0.85 | 1.16 |
| 11-02 04:50 | +20 | BNB | DOWN | 0.71 | 0.91 | 1.79 |
| 11-02 04:50 | +15 | BNB | DOWN | 0.71 | 0.86 | 1.26 |
| 11-02 04:50 | +10 | BNB | DOWN | 0.71 | 0.85 | 1.16 |
| 11-02 04:50 | +5 | BNB | DOWN | 0.71 | 0.85 | 1.16 |
| 11-02 04:50 | +10 stop | DOGE | DOWN | 0.70 | 0.89 | 1.68 |
| 11-02 04:50 | +5 | XRP | DOWN | 0.65 | 0.72 | 0.39 |
| 11-02 04:50 | +5 | BTC | UP | 0.49 | 0.57 | 0.44 |
| 11-02 04:49 | +10 stop | XRP | DOWN | 0.59 | 0.72 | 0.93 |
| 11-02 04:49 | +10 | XRP | DOWN | 0.58 | 0.72 | 1.03 |
| 11-02 04:49 | +10 stop | NEAR | DOWN | 0.67 | 0.78 | 0.81 |
| 11-02 04:49 | +10 stop | ETH | DOWN | 0.59 | 0.76 | 1.40 |
| 11-02 04:49 | +10 | ETH | DOWN | 0.60 | 0.76 | 1.30 |
| 11-02 04:49 | +5 | ETH | DOWN | 0.58 | 0.64 | 0.25 |
| 11-02 04:49 | +10 stop | SOL | DOWN | 0.58 | 0.73 | 1.18 |
| 11-02 04:49 | +5 | XRP | DOWN | 0.54 | 0.68 | 1.06 |
| 11-02 04:49 | +10 stop | ZEC | UP | 0.70 | 0.45 | -2.83 |
| 11-02 04:49 | +10 | ZEC | UP | 0.70 | 0.86 | 1.36 |
| 11-02 04:49 | +5 | ZEC | UP | 0.70 | 0.86 | 1.36 |
| 11-02 04:49 | +10 stop | BTC | UP | 0.51 | 0.36 | -1.85 |
| 11-02 04:49 | +10 | BTC | UP | 0.51 | open |  |
| 11-02 04:49 | +5 | BTC | UP | 0.58 | 0.69 | 0.77 |
| 11-02 04:48 | +10 stop | HYPE | DOWN | 0.56 | 0.66 | 0.66 |
| 11-02 04:48 | +10 stop | NEAR | UP | 0.52 | 0.34 | -2.14 |
| 11-02 04:48 | +20 | NEAR | UP | 0.52 | open |  |
| 11-02 04:48 | +15 | NEAR | UP | 0.52 | open |  |
| 11-02 04:48 | +10 | NEAR | UP | 0.52 | open |  |
| 11-02 04:48 | +5 | NEAR | UP | 0.52 | open |  |
| 11-02 04:46 | +10 stop | SOL | UP | 0.69 | 0.45 | -2.73 |
| 11-02 04:46 | +20 | SOL | UP | 0.69 | open |  |
| 11-02 04:46 | +15 | SOL | UP | 0.69 | open |  |
| 11-02 04:46 | +10 | SOL | UP | 0.69 | open |  |
| 11-02 04:46 | +5 | SOL | UP | 0.69 | open |  |
| 11-02 04:46 | +10 stop | DOGE | UP | 0.65 | 0.32 | -3.62 |
| 11-02 04:46 | +20 | DOGE | UP | 0.65 | open |  |
| 11-02 04:46 | +15 | DOGE | UP | 0.65 | open |  |

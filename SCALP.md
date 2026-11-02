# Range-Scalp Bot

*Updated Mon Nov 02 22:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45253 | 39410 | 5843 (67) | 2 | $-13041.77 | -4.6% |
| **+10¢** | 33772 | 27001 | 6771 (88) | 2 | $-11921.72 | -5.6% |
| **+15¢** | 28250 | 20963 | 7287 (115) | 2 | $-10969.30 | -6.2% |
| **+20¢** | 25087 | 17455 | 7632 (150) | 2 | $-9729.53 | -6.2% |
| **+10¢ (15¢ stop)** | 55196 | 55109 | 87 (51) | 0 | $-20841.90 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 22:42 | +10 stop | BNB | UP | 0.69 | 0.80 | 0.83 |
| 11-02 22:42 | +10 | BNB | UP | 0.69 | 0.80 | 0.83 |
| 11-02 22:42 | +5 | BNB | UP | 0.69 | 0.80 | 0.83 |
| 11-02 22:40 | +10 stop | BNB | UP | 0.62 | 0.76 | 1.10 |
| 11-02 22:40 | +20 | BNB | UP | 0.62 | 0.83 | 1.83 |
| 11-02 22:40 | +15 | BNB | UP | 0.62 | 0.80 | 1.51 |
| 11-02 22:40 | +10 | BNB | UP | 0.62 | 0.76 | 1.10 |
| 11-02 22:40 | +5 | BNB | UP | 0.62 | 0.76 | 1.10 |
| 11-02 22:40 | +10 stop | XRP | UP | 0.61 | 0.73 | 0.89 |
| 11-02 22:40 | +5 | XRP | UP | 0.61 | 0.73 | 0.89 |
| 11-02 22:40 | +10 stop | SOL | UP | 0.63 | 0.76 | 1.00 |
| 11-02 22:40 | +20 | SOL | UP | 0.65 | 0.91 | 2.32 |
| 11-02 22:40 | +15 | SOL | UP | 0.65 | 0.91 | 2.32 |
| 11-02 22:40 | +10 | SOL | UP | 0.65 | 0.76 | 0.81 |
| 11-02 22:40 | +5 | SOL | UP | 0.64 | 0.76 | 0.90 |
| 11-02 22:39 | +10 stop | DOGE | UP | 0.67 | 0.78 | 0.81 |
| 11-02 22:37 | +5 | BNB | DOWN | 0.65 | 0.73 | 0.50 |
| 11-02 22:36 | +10 stop | DOGE | DOWN | 0.59 | 0.37 | -2.54 |
| 11-02 22:35 | +10 stop | DOGE | UP | 0.63 | 0.44 | -2.25 |
| 11-02 22:34 | +10 stop | XRP | DOWN | 0.57 | 0.31 | -2.93 |
| 11-02 22:34 | +5 | ZEC | UP | 0.60 | open |  |
| 11-02 22:34 | +10 stop | SOL | DOWN | 0.57 | 0.72 | 1.17 |
| 11-02 22:34 | +20 | SOL | DOWN | 0.57 | 0.78 | 1.79 |
| 11-02 22:34 | +15 | SOL | DOWN | 0.57 | 0.72 | 1.17 |
| 11-02 22:34 | +10 | SOL | DOWN | 0.57 | 0.72 | 1.17 |
| 11-02 22:34 | +5 | SOL | DOWN | 0.57 | 0.66 | 0.56 |
| 11-02 22:34 | +10 stop | BNB | DOWN | 0.59 | 0.73 | 1.09 |
| 11-02 22:34 | +20 | BNB | DOWN | 0.59 | 0.80 | 1.81 |
| 11-02 22:34 | +15 | BNB | DOWN | 0.59 | 0.74 | 1.19 |
| 11-02 22:34 | +10 | BNB | DOWN | 0.59 | 0.73 | 1.09 |
| 11-02 22:34 | +5 | BNB | DOWN | 0.59 | 0.67 | 0.47 |
| 11-02 22:33 | +10 stop | DOGE | DOWN | 0.63 | 0.37 | -2.94 |
| 11-02 22:33 | +20 | DOGE | DOWN | 0.63 | open |  |
| 11-02 22:33 | +15 | DOGE | DOWN | 0.63 | open |  |
| 11-02 22:33 | +10 | DOGE | DOWN | 0.62 | open |  |
| 11-02 22:33 | +5 | DOGE | DOWN | 0.62 | open |  |
| 11-02 22:33 | +5 | ZEC | UP | 0.55 | 0.60 | 0.15 |
| 11-02 22:32 | +10 stop | XRP | DOWN | 0.70 | 0.54 | -1.93 |
| 11-02 22:32 | +10 stop | BTC | DOWN | 0.70 | 0.83 | 1.05 |
| 11-02 22:32 | +20 | BTC | DOWN | 0.70 | 0.90 | 1.79 |

# Range-Scalp Bot

*Updated Mon Nov 02 23:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45264 | 39416 | 5848 (67) | 3 | $-13067.86 | -4.6% |
| **+10¢** | 33782 | 27006 | 6776 (88) | 4 | $-11946.52 | -5.6% |
| **+15¢** | 28258 | 20966 | 7292 (115) | 5 | $-10994.02 | -6.2% |
| **+20¢** | 25095 | 17458 | 7637 (150) | 5 | $-9753.49 | -6.2% |
| **+10¢ (15¢ stop)** | 55210 | 55123 | 87 (51) | 4 | $-20846.28 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 23:03 | +10 stop | ZEC | DOWN | 0.60 | open |  |
| 11-02 23:03 | +20 | ZEC | DOWN | 0.61 | open |  |
| 11-02 23:03 | +15 | ZEC | DOWN | 0.62 | open |  |
| 11-02 23:03 | +10 | ZEC | DOWN | 0.62 | open |  |
| 11-02 23:03 | +5 | ZEC | DOWN | 0.62 | 0.68 | 0.27 |
| 11-02 23:03 | +10 stop | XRP | DOWN | 0.69 | open |  |
| 11-02 23:03 | +20 | XRP | DOWN | 0.69 | open |  |
| 11-02 23:03 | +15 | XRP | DOWN | 0.68 | open |  |
| 11-02 23:03 | +10 | XRP | DOWN | 0.68 | open |  |
| 11-02 23:03 | +5 | XRP | DOWN | 0.68 | open |  |
| 11-02 23:03 | +10 stop | DOGE | DOWN | 0.57 | open |  |
| 11-02 23:03 | +20 | DOGE | DOWN | 0.57 | open |  |
| 11-02 23:03 | +15 | DOGE | DOWN | 0.57 | open |  |
| 11-02 23:03 | +10 | DOGE | DOWN | 0.57 | open |  |
| 11-02 23:03 | +5 | DOGE | DOWN | 0.57 | open |  |
| 11-02 23:03 | +10 stop | HYPE | DOWN | 0.62 | open |  |
| 11-02 23:03 | +20 | HYPE | DOWN | 0.62 | open |  |
| 11-02 23:03 | +15 | HYPE | DOWN | 0.62 | open |  |
| 11-02 23:03 | +10 | HYPE | DOWN | 0.60 | 0.71 | 0.75 |
| 11-02 23:03 | +5 | HYPE | DOWN | 0.60 | 0.67 | 0.34 |
| 11-02 23:02 | +10 stop | NEAR | DOWN | 0.70 | 0.48 | -2.53 |
| 11-02 23:02 | +20 | NEAR | DOWN | 0.70 | open |  |
| 11-02 23:02 | +15 | NEAR | DOWN | 0.70 | open |  |
| 11-02 23:02 | +10 | NEAR | DOWN | 0.71 | open |  |
| 11-02 23:02 | +5 | NEAR | DOWN | 0.70 | open |  |
| 11-02 23:00 | +10 stop | HYPE | DOWN | 0.63 | 0.74 | 0.79 |
| 11-02 23:00 | +20 | HYPE | DOWN | 0.63 | 0.88 | 2.25 |
| 11-02 23:00 | +15 | HYPE | DOWN | 0.63 | 0.81 | 1.52 |
| 11-02 23:00 | +10 | HYPE | DOWN | 0.63 | 0.74 | 0.79 |
| 11-02 23:00 | +5 | HYPE | DOWN | 0.62 | 0.74 | 0.87 |
| 11-02 22:57 | +10 stop | XRP | UP | 0.65 | 0.85 | 1.75 |
| 11-02 22:55 | +10 stop | XRP | UP | 0.64 | 0.44 | -2.35 |
| 11-02 22:53 | +10 stop | XRP | UP | 0.66 | 0.78 | 0.91 |
| 11-02 22:51 | +10 stop | DOGE | UP | 0.70 | 0.81 | 0.84 |
| 11-02 22:51 | +10 | DOGE | UP | 0.70 | 0.81 | 0.84 |
| 11-02 22:51 | +5 | DOGE | UP | 0.70 | 0.77 | 0.42 |
| 11-02 22:50 | +10 stop | NEAR | DOWN | 0.66 | 0.49 | -2.04 |
| 11-02 22:48 | +10 stop | XRP | UP | 0.55 | 0.66 | 0.76 |
| 11-02 22:48 | +10 stop | BNB | UP | 0.68 | 0.80 | 0.92 |
| 11-02 22:47 | +10 stop | NEAR | UP | 0.56 | 0.40 | -1.93 |

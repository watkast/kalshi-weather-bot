# Range-Scalp Bot

*Updated Mon Nov 02 22:54 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45258 | 39413 | 5845 (67) | 3 | $-13052.00 | -4.6% |
| **+10¢** | 33777 | 27004 | 6773 (88) | 3 | $-11930.72 | -5.6% |
| **+15¢** | 28254 | 20965 | 7289 (115) | 3 | $-10978.30 | -6.2% |
| **+20¢** | 25091 | 17457 | 7634 (150) | 3 | $-9738.32 | -6.2% |
| **+10¢ (15¢ stop)** | 55206 | 55119 | 87 (51) | 0 | $-20843.94 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 22:53 | +10 stop | XRP | UP | 0.66 | 0.78 | 0.91 |
| 11-02 22:51 | +10 stop | DOGE | UP | 0.70 | 0.81 | 0.84 |
| 11-02 22:51 | +10 | DOGE | UP | 0.70 | 0.81 | 0.84 |
| 11-02 22:51 | +5 | DOGE | UP | 0.70 | 0.77 | 0.42 |
| 11-02 22:50 | +10 stop | NEAR | DOWN | 0.66 | 0.49 | -2.04 |
| 11-02 22:48 | +10 stop | XRP | UP | 0.55 | 0.66 | 0.76 |
| 11-02 22:48 | +10 stop | BNB | UP | 0.68 | 0.80 | 0.92 |
| 11-02 22:47 | +10 stop | NEAR | UP | 0.56 | 0.40 | -1.93 |
| 11-02 22:47 | +20 | NEAR | UP | 0.56 | open |  |
| 11-02 22:47 | +15 | NEAR | UP | 0.53 | open |  |
| 11-02 22:47 | +10 | NEAR | UP | 0.53 | open |  |
| 11-02 22:47 | +5 | NEAR | UP | 0.53 | open |  |
| 11-02 22:46 | +10 stop | DOGE | UP | 0.68 | 0.79 | 0.82 |
| 11-02 22:46 | +20 | DOGE | UP | 0.68 | 0.88 | 1.76 |
| 11-02 22:46 | +15 | DOGE | UP | 0.68 | 0.88 | 1.76 |
| 11-02 22:46 | +10 | DOGE | UP | 0.68 | 0.79 | 0.82 |
| 11-02 22:46 | +5 | DOGE | UP | 0.68 | 0.74 | 0.30 |
| 11-02 22:46 | +10 stop | BNB | DOWN | 0.56 | 0.40 | -1.95 |
| 11-02 22:46 | +20 | BNB | DOWN | 0.56 | open |  |
| 11-02 22:46 | +15 | BNB | DOWN | 0.57 | open |  |
| 11-02 22:46 | +10 | BNB | DOWN | 0.57 | open |  |
| 11-02 22:46 | +5 | BNB | DOWN | 0.57 | open |  |
| 11-02 22:46 | +10 stop | XRP | DOWN | 0.58 | 0.42 | -1.96 |
| 11-02 22:46 | +20 | XRP | DOWN | 0.57 | open |  |
| 11-02 22:46 | +15 | XRP | DOWN | 0.57 | open |  |
| 11-02 22:46 | +10 | XRP | DOWN | 0.58 | open |  |
| 11-02 22:46 | +5 | XRP | DOWN | 0.58 | open |  |
| 11-02 22:46 | +10 stop | BTC | UP | 0.58 | 0.77 | 1.59 |
| 11-02 22:46 | +20 | BTC | UP | 0.58 | 0.79 | 1.80 |
| 11-02 22:46 | +15 | BTC | UP | 0.58 | 0.77 | 1.59 |
| 11-02 22:46 | +10 | BTC | UP | 0.58 | 0.77 | 1.59 |
| 11-02 22:46 | +5 | BTC | UP | 0.58 | 0.77 | 1.59 |
| 11-02 22:42 | +10 stop | BNB | UP | 0.69 | 0.80 | 0.83 |
| 11-02 22:42 | +10 | BNB | UP | 0.69 | 0.80 | 0.83 |
| 11-02 22:42 | +5 | BNB | UP | 0.69 | 0.80 | 0.83 |
| 11-02 22:40 | +10 stop | BNB | UP | 0.62 | 0.76 | 1.10 |
| 11-02 22:40 | +20 | BNB | UP | 0.62 | 0.83 | 1.83 |
| 11-02 22:40 | +15 | BNB | UP | 0.62 | 0.80 | 1.51 |
| 11-02 22:40 | +10 | BNB | UP | 0.62 | 0.76 | 1.10 |
| 11-02 22:40 | +5 | BNB | UP | 0.62 | 0.76 | 1.10 |

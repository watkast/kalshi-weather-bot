# Range-Scalp Bot

*Updated Mon Nov 02 12:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44821 | 39029 | 5792 (65) | 3 | $-12965.81 | -4.6% |
| **+10¢** | 33462 | 26754 | 6708 (86) | 3 | $-11809.44 | -5.6% |
| **+15¢** | 27992 | 20773 | 7219 (113) | 4 | $-10854.38 | -6.2% |
| **+20¢** | 24869 | 17312 | 7557 (148) | 4 | $-9579.55 | -6.1% |
| **+10¢ (15¢ stop)** | 54708 | 54621 | 87 (51) | 3 | $-20685.62 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 12:01 | +10 stop | DOGE | DOWN | 0.51 | open |  |
| 11-02 12:01 | +20 | DOGE | DOWN | 0.51 | open |  |
| 11-02 12:01 | +15 | DOGE | DOWN | 0.51 | open |  |
| 11-02 12:01 | +10 | DOGE | DOWN | 0.51 | open |  |
| 11-02 12:01 | +5 | DOGE | DOWN | 0.51 | open |  |
| 11-02 12:01 | +10 stop | XRP | DOWN | 0.44 | open |  |
| 11-02 12:01 | +10 | XRP | DOWN | 0.44 | open |  |
| 11-02 12:01 | +5 | XRP | DOWN | 0.44 | open |  |
| 11-02 12:01 | +10 stop | XRP | UP | 0.44 | 0.55 | 0.74 |
| 11-02 12:01 | +20 | XRP | UP | 0.45 | open |  |
| 11-02 12:01 | +15 | XRP | UP | 0.45 | open |  |
| 11-02 12:01 | +10 | XRP | UP | 0.45 | 0.55 | 0.69 |
| 11-02 12:01 | +5 | XRP | UP | 0.44 | 0.55 | 0.74 |
| 11-02 12:01 | +10 stop | SOL | UP | 0.57 | open |  |
| 11-02 12:01 | +20 | SOL | UP | 0.57 | open |  |
| 11-02 12:01 | +15 | SOL | UP | 0.57 | open |  |
| 11-02 12:01 | +10 | SOL | UP | 0.57 | open |  |
| 11-02 12:01 | +5 | SOL | UP | 0.57 | open |  |
| 11-02 12:00 | +10 stop | BNB | DOWN | 0.52 | 0.63 | 0.75 |
| 11-02 12:00 | +20 | BNB | DOWN | 0.52 | open |  |
| 11-02 12:00 | +15 | BNB | DOWN | 0.52 | open |  |
| 11-02 12:00 | +10 | BNB | DOWN | 0.52 | 0.63 | 0.75 |
| 11-02 12:00 | +5 | BNB | DOWN | 0.52 | 0.63 | 0.75 |
| 11-02 11:58 | +10 stop | ETH | DOWN | 0.64 | 0.23 | -4.40 |
| 11-02 11:56 | +10 stop | BTC | UP | 0.49 | 0.65 | 1.26 |
| 11-02 11:56 | +10 | BTC | UP | 0.49 | 0.65 | 1.26 |
| 11-02 11:56 | +10 stop | HYPE | UP | 0.61 | 0.39 | -2.54 |
| 11-02 11:56 | +10 stop | BTC | DOWN | 0.41 | 0.55 | 1.05 |
| 11-02 11:56 | +20 | BTC | DOWN | 0.41 | 0.70 | 2.58 |
| 11-02 11:56 | +15 | BTC | DOWN | 0.41 | 0.70 | 2.58 |
| 11-02 11:56 | +10 | BTC | DOWN | 0.41 | 0.55 | 1.05 |
| 11-02 11:55 | +10 stop | NEAR | DOWN | 0.60 | 0.89 | 2.66 |
| 11-02 11:55 | +5 | BTC | DOWN | 0.71 | 0.82 | 0.84 |
| 11-02 11:54 | +10 stop | HYPE | DOWN | 0.66 | 0.43 | -2.64 |
| 11-02 11:54 | +20 | HYPE | DOWN | 0.65 | 0.85 | 1.75 |
| 11-02 11:54 | +15 | HYPE | DOWN | 0.65 | 0.85 | 1.75 |
| 11-02 11:54 | +10 | HYPE | DOWN | 0.65 | 0.85 | 1.75 |
| 11-02 11:54 | +5 | HYPE | DOWN | 0.69 | 0.85 | 1.34 |
| 11-02 11:54 | +10 stop | BTC | DOWN | 0.54 | 0.64 | 0.65 |
| 11-02 11:54 | +20 | BTC | DOWN | 0.54 | 0.75 | 1.78 |

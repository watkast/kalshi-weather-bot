# Range-Scalp Bot

*Updated Mon Nov 02 02:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44260 | 38546 | 5714 (65) | 2 | $-12777.71 | -4.6% |
| **+10¢** | 33029 | 26422 | 6607 (86) | 3 | $-11560.50 | -5.6% |
| **+15¢** | 27645 | 20534 | 7111 (113) | 3 | $-10573.91 | -6.1% |
| **+20¢** | 24566 | 17123 | 7443 (147) | 4 | $-9286.45 | -6.0% |
| **+10¢ (15¢ stop)** | 53995 | 53909 | 86 (51) | 0 | $-20462.75 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 02:42 | +10 stop | BTC | UP | 0.63 | 0.73 | 0.69 |
| 11-02 02:42 | +10 | BTC | UP | 0.61 | 0.73 | 0.89 |
| 11-02 02:38 | +10 stop | HYPE | DOWN | 0.58 | 0.43 | -1.86 |
| 11-02 02:38 | +20 | HYPE | DOWN | 0.56 | open |  |
| 11-02 02:38 | +15 | HYPE | DOWN | 0.56 | open |  |
| 11-02 02:38 | +10 | HYPE | DOWN | 0.56 | open |  |
| 11-02 02:38 | +5 | HYPE | DOWN | 0.56 | 0.63 | 0.35 |
| 11-02 02:32 | +10 stop | BNB | DOWN | 0.59 | 0.94 | 3.31 |
| 11-02 02:32 | +20 | BNB | DOWN | 0.59 | 0.94 | 3.31 |
| 11-02 02:32 | +15 | BNB | DOWN | 0.59 | 0.94 | 3.31 |
| 11-02 02:32 | +10 | BNB | DOWN | 0.59 | 0.94 | 3.31 |
| 11-02 02:32 | +5 | BNB | DOWN | 0.59 | 0.94 | 3.31 |
| 11-02 02:32 | +10 stop | ETH | DOWN | 0.59 | 0.93 | 3.17 |
| 11-02 02:32 | +20 | ETH | DOWN | 0.59 | 0.93 | 3.17 |
| 11-02 02:32 | +15 | ETH | DOWN | 0.59 | 0.93 | 3.17 |
| 11-02 02:32 | +10 | ETH | DOWN | 0.59 | 0.93 | 3.17 |
| 11-02 02:32 | +5 | ETH | DOWN | 0.59 | 0.67 | 0.47 |
| 11-02 02:32 | +10 stop | HYPE | DOWN | 0.65 | 0.84 | 1.60 |
| 11-02 02:31 | +5 | BTC | UP | 0.65 | 0.73 | 0.50 |
| 11-02 02:31 | +10 stop | XRP | UP | 0.61 | 0.46 | -1.85 |
| 11-02 02:31 | +10 | XRP | UP | 0.61 | 0.76 | 1.20 |
| 11-02 02:31 | +10 stop | ZEC | UP | 0.64 | 0.40 | -2.74 |
| 11-02 02:31 | +20 | ZEC | UP | 0.64 | open |  |
| 11-02 02:31 | +15 | ZEC | UP | 0.64 | open |  |
| 11-02 02:31 | +10 | ZEC | UP | 0.64 | open |  |
| 11-02 02:31 | +5 | ZEC | UP | 0.64 | open |  |
| 11-02 02:31 | +10 stop | SOL | UP | 0.62 | 0.43 | -2.25 |
| 11-02 02:31 | +20 | SOL | UP | 0.62 | open |  |
| 11-02 02:31 | +15 | SOL | UP | 0.62 | open |  |
| 11-02 02:31 | +10 | SOL | UP | 0.62 | open |  |
| 11-02 02:31 | +5 | SOL | UP | 0.62 | open |  |
| 11-02 02:31 | +5 | XRP | UP | 0.58 | 0.76 | 1.46 |
| 11-02 02:31 | +10 stop | DOGE | DOWN | 0.62 | 0.73 | 0.79 |
| 11-02 02:31 | +20 | DOGE | DOWN | 0.62 | 0.92 | 2.79 |
| 11-02 02:31 | +15 | DOGE | DOWN | 0.63 | 0.92 | 2.69 |
| 11-02 02:31 | +10 | DOGE | DOWN | 0.63 | 0.73 | 0.69 |
| 11-02 02:31 | +5 | DOGE | DOWN | 0.63 | 0.73 | 0.69 |
| 11-02 02:31 | +10 stop | BTC | UP | 0.52 | 0.19 | -3.59 |
| 11-02 02:31 | +20 | BTC | UP | 0.52 | 0.73 | 1.78 |
| 11-02 02:31 | +15 | BTC | UP | 0.52 | 0.68 | 1.26 |

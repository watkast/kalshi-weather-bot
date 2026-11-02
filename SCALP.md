# Range-Scalp Bot

*Updated Mon Nov 02 05:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44467 | 38719 | 5748 (65) | 1 | $-12872.82 | -4.6% |
| **+10¢** | 33192 | 26545 | 6647 (86) | 3 | $-11659.20 | -5.6% |
| **+15¢** | 27788 | 20635 | 7153 (113) | 3 | $-10668.63 | -6.1% |
| **+20¢** | 24699 | 17212 | 7487 (147) | 3 | $-9367.23 | -6.0% |
| **+10¢ (15¢ stop)** | 54280 | 54194 | 86 (51) | 1 | $-20630.52 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 05:37 | +5 | BTC | UP | 0.67 | 0.72 | 0.19 |
| 11-02 05:33 | +10 stop | BTC | UP | 0.69 | open |  |
| 11-02 05:33 | +5 | BTC | UP | 0.69 | 0.74 | 0.21 |
| 11-02 05:32 | +10 stop | DOGE | UP | 0.65 | 0.79 | 1.12 |
| 11-02 05:32 | +10 stop | BTC | UP | 0.57 | 0.68 | 0.76 |
| 11-02 05:32 | +10 stop | SOL | UP | 0.57 | 0.72 | 1.17 |
| 11-02 05:32 | +20 | SOL | UP | 0.57 | 0.80 | 2.00 |
| 11-02 05:32 | +15 | SOL | UP | 0.57 | 0.72 | 1.17 |
| 11-02 05:32 | +10 | SOL | UP | 0.57 | 0.72 | 1.17 |
| 11-02 05:32 | +5 | SOL | UP | 0.57 | 0.72 | 1.17 |
| 11-02 05:32 | +10 stop | BNB | UP | 0.64 | 0.82 | 1.52 |
| 11-02 05:32 | +20 | BNB | UP | 0.64 | 0.85 | 1.84 |
| 11-02 05:32 | +15 | BNB | UP | 0.64 | 0.82 | 1.52 |
| 11-02 05:32 | +10 | BNB | UP | 0.64 | 0.82 | 1.52 |
| 11-02 05:32 | +5 | BNB | UP | 0.64 | 0.69 | 0.18 |
| 11-02 05:32 | +5 | BTC | UP | 0.60 | 0.68 | 0.47 |
| 11-02 05:32 | +10 stop | HYPE | UP | 0.66 | 0.78 | 0.91 |
| 11-02 05:32 | +20 | HYPE | UP | 0.66 | 0.91 | 2.31 |
| 11-02 05:32 | +15 | HYPE | UP | 0.66 | 0.83 | 1.44 |
| 11-02 05:32 | +10 | HYPE | UP | 0.66 | 0.78 | 0.91 |
| 11-02 05:32 | +5 | HYPE | UP | 0.66 | 0.78 | 0.91 |
| 11-02 05:31 | +10 stop | BTC | DOWN | 0.53 | 0.37 | -1.95 |
| 11-02 05:31 | +20 | BTC | DOWN | 0.52 | open |  |
| 11-02 05:31 | +15 | BTC | DOWN | 0.52 | open |  |
| 11-02 05:31 | +10 | BTC | DOWN | 0.52 | open |  |
| 11-02 05:31 | +5 | BTC | DOWN | 0.52 | 0.57 | 0.14 |
| 11-02 05:31 | +10 stop | DOGE | DOWN | 0.58 | 0.30 | -3.13 |
| 11-02 05:31 | +20 | DOGE | DOWN | 0.58 | open |  |
| 11-02 05:31 | +15 | DOGE | DOWN | 0.58 | open |  |
| 11-02 05:31 | +10 | DOGE | DOWN | 0.58 | open |  |
| 11-02 05:31 | +5 | DOGE | DOWN | 0.58 | open |  |
| 11-02 05:31 | +10 stop | XRP | UP | 0.62 | 0.77 | 1.20 |
| 11-02 05:31 | +20 | XRP | UP | 0.62 | 0.85 | 2.04 |
| 11-02 05:31 | +15 | XRP | UP | 0.62 | 0.77 | 1.20 |
| 11-02 05:31 | +10 | XRP | UP | 0.62 | 0.77 | 1.20 |
| 11-02 05:31 | +5 | XRP | UP | 0.62 | 0.68 | 0.27 |
| 11-02 05:31 | +10 stop | NEAR | UP | 0.67 | 0.81 | 1.13 |
| 11-02 05:31 | +20 | NEAR | UP | 0.68 | 0.88 | 1.76 |
| 11-02 05:31 | +15 | NEAR | UP | 0.68 | 0.83 | 1.24 |
| 11-02 05:31 | +10 | NEAR | UP | 0.68 | 0.81 | 1.03 |

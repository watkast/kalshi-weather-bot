# Range-Scalp Bot

*Updated Mon Nov 02 06:18 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44526 | 38774 | 5752 (65) | 4 | $-12864.93 | -4.6% |
| **+10¢** | 33231 | 26577 | 6654 (86) | 5 | $-11666.26 | -5.6% |
| **+15¢** | 27818 | 20657 | 7161 (113) | 6 | $-10678.72 | -6.1% |
| **+20¢** | 24724 | 17228 | 7496 (147) | 7 | $-9383.95 | -6.0% |
| **+10¢ (15¢ stop)** | 54348 | 54262 | 86 (51) | 3 | $-20629.63 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 06:18 | +5 | ETH | DOWN | 0.69 | 0.75 | 0.31 |
| 11-02 06:18 | +10 stop | BNB | DOWN | 0.64 | open |  |
| 11-02 06:17 | +5 | ETH | DOWN | 0.59 | 0.64 | 0.16 |
| 11-02 06:17 | +10 stop | SOL | DOWN | 0.57 | 0.72 | 1.17 |
| 11-02 06:17 | +10 stop | HYPE | DOWN | 0.50 | open |  |
| 11-02 06:17 | +5 | SOL | DOWN | 0.57 | 0.72 | 1.17 |
| 11-02 06:17 | +10 stop | ETH | DOWN | 0.58 | 0.75 | 1.38 |
| 11-02 06:17 | +20 | ETH | DOWN | 0.58 | open |  |
| 11-02 06:17 | +15 | ETH | DOWN | 0.58 | 0.75 | 1.38 |
| 11-02 06:17 | +10 | ETH | DOWN | 0.58 | 0.75 | 1.38 |
| 11-02 06:17 | +5 | ETH | DOWN | 0.58 | 0.63 | 0.15 |
| 11-02 06:17 | +10 stop | ZEC | UP | 0.59 | open |  |
| 11-02 06:17 | +20 | ZEC | UP | 0.59 | open |  |
| 11-02 06:17 | +15 | ZEC | UP | 0.59 | open |  |
| 11-02 06:17 | +10 | ZEC | UP | 0.59 | open |  |
| 11-02 06:17 | +5 | ZEC | UP | 0.59 | open |  |
| 11-02 06:17 | +10 stop | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 11-02 06:17 | +20 | XRP | DOWN | 0.63 | open |  |
| 11-02 06:17 | +15 | XRP | DOWN | 0.63 | open |  |
| 11-02 06:17 | +10 | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 11-02 06:17 | +5 | XRP | DOWN | 0.63 | 0.69 | 0.28 |
| 11-02 06:16 | +10 stop | NEAR | UP | 0.58 | 0.41 | -2.05 |
| 11-02 06:16 | +20 | NEAR | UP | 0.58 | open |  |
| 11-02 06:16 | +15 | NEAR | UP | 0.58 | open |  |
| 11-02 06:16 | +10 | NEAR | UP | 0.58 | open |  |
| 11-02 06:16 | +5 | NEAR | UP | 0.58 | open |  |
| 11-02 06:16 | +10 stop | HYPE | UP | 0.66 | 0.46 | -2.34 |
| 11-02 06:16 | +20 | HYPE | UP | 0.66 | open |  |
| 11-02 06:16 | +15 | HYPE | UP | 0.66 | open |  |
| 11-02 06:16 | +10 | HYPE | UP | 0.66 | open |  |
| 11-02 06:16 | +5 | HYPE | UP | 0.66 | open |  |
| 11-02 06:16 | +10 stop | SOL | UP | 0.58 | 0.40 | -2.15 |
| 11-02 06:16 | +20 | SOL | UP | 0.58 | open |  |
| 11-02 06:16 | +15 | SOL | UP | 0.58 | open |  |
| 11-02 06:16 | +10 | SOL | UP | 0.58 | open |  |
| 11-02 06:16 | +5 | SOL | UP | 0.58 | 0.64 | 0.25 |
| 11-02 06:16 | +10 stop | BNB | UP | 0.51 | 0.35 | -1.94 |
| 11-02 06:16 | +20 | BNB | UP | 0.51 | open |  |
| 11-02 06:16 | +15 | BNB | UP | 0.51 | open |  |
| 11-02 06:16 | +10 | BNB | UP | 0.51 | open |  |

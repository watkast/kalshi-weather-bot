# Range-Scalp Bot

*Updated Mon Nov 02 04:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44359 | 38628 | 5731 (65) | 2 | $-12838.60 | -4.6% |
| **+10¢** | 33110 | 26484 | 6626 (86) | 2 | $-11611.74 | -5.6% |
| **+15¢** | 27719 | 20589 | 7130 (113) | 3 | $-10605.52 | -6.1% |
| **+20¢** | 24630 | 17169 | 7461 (147) | 6 | $-9303.04 | -6.0% |
| **+10¢ (15¢ stop)** | 54140 | 54054 | 86 (51) | 2 | $-20556.85 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 04:06 | +5 | BNB | DOWN | 0.60 | open |  |
| 11-02 04:06 | +15 | BTC | DOWN | 0.67 | open |  |
| 11-02 04:04 | +5 | ZEC | DOWN | 0.58 | 0.63 | 0.15 |
| 11-02 04:04 | +10 stop | ZEC | DOWN | 0.62 | 0.74 | 0.89 |
| 11-02 04:04 | +10 stop | SOL | DOWN | 0.64 | 0.74 | 0.69 |
| 11-02 04:04 | +5 | XRP | DOWN | 0.70 | 0.75 | 0.21 |
| 11-02 04:04 | +10 stop | BTC | DOWN | 0.66 | open |  |
| 11-02 04:04 | +10 | BTC | DOWN | 0.65 | open |  |
| 11-02 04:04 | +10 stop | ETH | DOWN | 0.60 | 0.73 | 0.99 |
| 11-02 04:04 | +10 stop | DOGE | DOWN | 0.71 | 0.84 | 1.05 |
| 11-02 04:04 | +10 | DOGE | DOWN | 0.71 | 0.84 | 1.05 |
| 11-02 04:03 | +10 stop | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 11-02 04:03 | +5 | BTC | DOWN | 0.68 | 0.73 | 0.20 |
| 11-02 04:03 | +5 | DOGE | DOWN | 0.70 | 0.75 | 0.21 |
| 11-02 04:02 | +10 stop | SOL | UP | 0.52 | 0.37 | -1.85 |
| 11-02 04:02 | +10 stop | ETH | UP | 0.53 | 0.36 | -2.05 |
| 11-02 04:02 | +5 | ETH | UP | 0.54 | open |  |
| 11-02 04:02 | +10 stop | ZEC | UP | 0.54 | 0.38 | -1.95 |
| 11-02 04:02 | +10 stop | XRP | UP | 0.60 | 0.41 | -2.24 |
| 11-02 04:02 | +10 stop | NEAR | DOWN | 0.65 | 0.75 | 0.70 |
| 11-02 04:02 | +20 | NEAR | DOWN | 0.65 | 0.88 | 2.06 |
| 11-02 04:02 | +15 | NEAR | DOWN | 0.65 | 0.81 | 1.33 |
| 11-02 04:02 | +10 | NEAR | DOWN | 0.63 | 0.73 | 0.69 |
| 11-02 04:02 | +5 | NEAR | DOWN | 0.63 | 0.73 | 0.69 |
| 11-02 04:01 | +10 stop | HYPE | DOWN | 0.45 | 0.25 | -2.36 |
| 11-02 04:01 | +20 | HYPE | DOWN | 0.45 | open |  |
| 11-02 04:01 | +15 | HYPE | DOWN | 0.45 | open |  |
| 11-02 04:01 | +10 | HYPE | DOWN | 0.45 | 0.55 | 0.64 |
| 11-02 04:01 | +5 | HYPE | DOWN | 0.45 | 0.55 | 0.64 |
| 11-02 04:01 | +10 stop | ZEC | DOWN | 0.62 | 0.45 | -2.05 |
| 11-02 04:01 | +20 | ZEC | DOWN | 0.62 | open |  |
| 11-02 04:01 | +15 | ZEC | DOWN | 0.62 | 0.79 | 1.41 |
| 11-02 04:01 | +10 | ZEC | DOWN | 0.62 | 0.74 | 0.89 |
| 11-02 04:01 | +5 | ZEC | DOWN | 0.62 | 0.69 | 0.38 |
| 11-02 04:01 | +5 | BNB | DOWN | 0.55 | 0.60 | 0.15 |
| 11-02 04:01 | +5 | XRP | DOWN | 0.56 | 0.63 | 0.35 |
| 11-02 04:01 | +5 | ETH | DOWN | 0.55 | 0.60 | 0.15 |
| 11-02 04:01 | +10 stop | SOL | DOWN | 0.64 | 0.42 | -2.55 |
| 11-02 04:01 | +20 | SOL | DOWN | 0.64 | open |  |
| 11-02 04:01 | +15 | SOL | DOWN | 0.64 | 0.81 | 1.42 |

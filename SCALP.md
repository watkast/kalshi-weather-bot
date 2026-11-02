# Range-Scalp Bot

*Updated Mon Nov 02 05:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44430 | 38684 | 5746 (65) | 4 | $-12894.43 | -4.6% |
| **+10¢** | 33163 | 26519 | 6644 (86) | 6 | $-11680.29 | -5.6% |
| **+15¢** | 27762 | 20612 | 7150 (113) | 6 | $-10688.94 | -6.1% |
| **+20¢** | 24673 | 17191 | 7482 (147) | 7 | $-9383.66 | -6.1% |
| **+10¢ (15¢ stop)** | 54225 | 54139 | 86 (51) | 3 | $-20597.87 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 05:06 | +20 | NEAR | DOWN | 0.63 | open |  |
| 11-02 05:06 | +15 | NEAR | DOWN | 0.63 | open |  |
| 11-02 05:06 | +5 | NEAR | DOWN | 0.63 | open |  |
| 11-02 05:06 | +10 stop | DOGE | UP | 0.62 | 0.75 | 0.99 |
| 11-02 05:06 | +10 stop | ETH | UP | 0.63 | open |  |
| 11-02 05:05 | +10 stop | SOL | UP | 0.70 | open |  |
| 11-02 05:05 | +20 | BTC | DOWN | 0.62 | open |  |
| 11-02 05:05 | +10 stop | ETH | DOWN | 0.59 | 0.37 | -2.54 |
| 11-02 05:05 | +20 | ETH | DOWN | 0.59 | open |  |
| 11-02 05:05 | +15 | ETH | DOWN | 0.59 | open |  |
| 11-02 05:05 | +10 | ETH | DOWN | 0.58 | open |  |
| 11-02 05:05 | +5 | ETH | DOWN | 0.58 | open |  |
| 11-02 05:04 | +15 | BTC | DOWN | 0.68 | open |  |
| 11-02 05:04 | +10 stop | BTC | DOWN | 0.62 | 0.44 | -2.15 |
| 11-02 05:03 | +10 stop | NEAR | DOWN | 0.69 | 0.52 | -2.03 |
| 11-02 05:03 | +10 | NEAR | DOWN | 0.69 | open |  |
| 11-02 05:03 | +5 | HYPE | DOWN | 0.65 | 0.72 | 0.39 |
| 11-02 05:03 | +5 | BNB | UP | 0.63 | 0.69 | 0.26 |
| 11-02 05:03 | +10 stop | DOGE | UP | 0.62 | 0.75 | 0.99 |
| 11-02 05:03 | +10 stop | HYPE | DOWN | 0.64 | open |  |
| 11-02 05:03 | +10 | HYPE | DOWN | 0.64 | open |  |
| 11-02 05:03 | +5 | HYPE | DOWN | 0.62 | 0.67 | 0.17 |
| 11-02 05:03 | +5 | XRP | DOWN | 0.56 | 0.71 | 1.17 |
| 11-02 05:03 | +5 | NEAR | DOWN | 0.60 | 0.66 | 0.27 |
| 11-02 05:02 | +10 stop | SOL | UP | 0.70 | 0.54 | -1.93 |
| 11-02 05:02 | +20 | SOL | UP | 0.69 | open |  |
| 11-02 05:02 | +15 | SOL | UP | 0.69 | open |  |
| 11-02 05:02 | +10 | SOL | UP | 0.69 | open |  |
| 11-02 05:02 | +5 | SOL | UP | 0.69 | 0.77 | 0.52 |
| 11-02 05:02 | +10 stop | BNB | UP | 0.60 | 0.73 | 0.99 |
| 11-02 05:02 | +20 | BNB | UP | 0.60 | open |  |
| 11-02 05:02 | +15 | BNB | UP | 0.60 | open |  |
| 11-02 05:02 | +10 | BNB | UP | 0.60 | 0.73 | 0.99 |
| 11-02 05:02 | +5 | BNB | UP | 0.60 | 0.66 | 0.27 |
| 11-02 05:02 | +10 stop | BTC | UP | 0.56 | 0.40 | -1.95 |
| 11-02 05:02 | +10 | BTC | UP | 0.56 | open |  |
| 11-02 05:02 | +5 | BTC | UP | 0.56 | open |  |
| 11-02 05:01 | +10 stop | ZEC | DOWN | 0.58 | 0.71 | 0.97 |
| 11-02 05:01 | +20 | ZEC | DOWN | 0.58 | 0.80 | 1.90 |
| 11-02 05:01 | +15 | ZEC | DOWN | 0.58 | 0.75 | 1.38 |

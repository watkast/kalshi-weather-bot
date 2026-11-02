# Range-Scalp Bot

*Updated Mon Nov 02 15:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45075 | 39245 | 5830 (67) | 1 | $-13062.49 | -4.6% |
| **+10¢** | 33644 | 26891 | 6753 (88) | 3 | $-11925.54 | -5.6% |
| **+15¢** | 28141 | 20875 | 7266 (115) | 3 | $-10976.49 | -6.2% |
| **+20¢** | 24990 | 17384 | 7606 (150) | 5 | $-9714.25 | -6.2% |
| **+10¢ (15¢ stop)** | 55022 | 54935 | 87 (51) | 0 | $-20841.66 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 15:28 | +5 | DOGE | DOWN | 0.36 | 0.57 | 1.75 |
| 11-02 15:28 | +10 stop | ZEC | UP | 0.66 | 0.95 | 2.71 |
| 11-02 15:28 | +5 | ZEC | UP | 0.69 | 0.95 | 2.42 |
| 11-02 15:28 | +10 stop | DOGE | DOWN | 0.58 | 0.31 | -3.02 |
| 11-02 15:28 | +5 | DOGE | DOWN | 0.58 | 0.64 | 0.26 |
| 11-02 15:27 | +5 | BTC | UP | 0.65 | 0.95 | 2.84 |
| 11-02 15:27 | +10 stop | NEAR | UP | 0.61 | 0.87 | 2.35 |
| 11-02 15:27 | +10 stop | DOGE | UP | 0.63 | 0.41 | -2.52 |
| 11-02 15:27 | +20 | DOGE | UP | 0.58 | open |  |
| 11-02 15:27 | +15 | DOGE | UP | 0.58 | open |  |
| 11-02 15:27 | +10 | DOGE | UP | 0.58 | open |  |
| 11-02 15:27 | +5 | DOGE | UP | 0.58 | 0.66 | 0.46 |
| 11-02 15:27 | +10 stop | BTC | UP | 0.69 | 0.95 | 2.45 |
| 11-02 15:27 | +10 stop | ZEC | DOWN | 0.50 | 0.33 | -2.04 |
| 11-02 15:27 | +15 | ZEC | DOWN | 0.50 | open |  |
| 11-02 15:27 | +10 | ZEC | DOWN | 0.48 | open |  |
| 11-02 15:27 | +5 | ZEC | DOWN | 0.49 | 0.57 | 0.44 |
| 11-02 15:26 | +10 | NEAR | DOWN | 0.53 | open |  |
| 11-02 15:26 | +5 | NEAR | DOWN | 0.67 | open |  |
| 11-02 15:26 | +10 stop | NEAR | DOWN | 0.60 | 0.39 | -2.44 |
| 11-02 15:25 | +5 | HYPE | UP | 0.63 | 0.74 | 0.79 |
| 11-02 15:25 | +10 stop | BNB | UP | 0.62 | 0.46 | -1.95 |
| 11-02 15:25 | +15 | BNB | UP | 0.63 | 0.83 | 1.73 |
| 11-02 15:25 | +10 | BNB | UP | 0.65 | 0.83 | 1.54 |
| 11-02 15:25 | +5 | BNB | UP | 0.65 | 0.72 | 0.39 |
| 11-02 15:25 | +10 stop | BTC | UP | 0.63 | 0.47 | -1.95 |
| 11-02 15:25 | +20 | BTC | UP | 0.63 | 0.95 | 3.03 |
| 11-02 15:25 | +15 | BTC | UP | 0.63 | 0.95 | 3.03 |
| 11-02 15:25 | +10 | BTC | UP | 0.63 | 0.95 | 3.03 |
| 11-02 15:25 | +10 stop | HYPE | UP | 0.59 | 0.74 | 1.19 |
| 11-02 15:25 | +15 | HYPE | UP | 0.59 | 0.74 | 1.19 |
| 11-02 15:25 | +10 | HYPE | UP | 0.59 | 0.74 | 1.19 |
| 11-02 15:25 | +5 | HYPE | UP | 0.59 | 0.66 | 0.37 |
| 11-02 15:25 | +10 stop | ETH | DOWN | 0.64 | 0.78 | 1.10 |
| 11-02 15:25 | +20 | ETH | DOWN | 0.60 | 0.88 | 2.55 |
| 11-02 15:25 | +15 | ETH | DOWN | 0.59 | 0.78 | 1.60 |
| 11-02 15:25 | +10 | ETH | DOWN | 0.59 | 0.78 | 1.60 |
| 11-02 15:25 | +5 | ETH | DOWN | 0.59 | 0.78 | 1.60 |
| 11-02 15:25 | +10 stop | ZEC | DOWN | 0.48 | 0.60 | 0.85 |
| 11-02 15:25 | +15 | ZEC | DOWN | 0.48 | 0.71 | 1.97 |

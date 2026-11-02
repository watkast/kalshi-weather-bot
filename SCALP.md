# Range-Scalp Bot

*Updated Mon Nov 02 12:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44849 | 39056 | 5793 (65) | 8 | $-12957.20 | -4.6% |
| **+10¢** | 33478 | 26769 | 6709 (86) | 9 | $-11800.43 | -5.6% |
| **+15¢** | 28005 | 20785 | 7220 (113) | 9 | $-10842.47 | -6.2% |
| **+20¢** | 24879 | 17320 | 7559 (148) | 9 | $-9573.61 | -6.1% |
| **+10¢ (15¢ stop)** | 54739 | 54652 | 87 (51) | 4 | $-20704.87 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 12:21 | +10 stop | BTC | DOWN | 0.61 | open |  |
| 11-02 12:21 | +5 | SOL | DOWN | 0.67 | open |  |
| 11-02 12:21 | +10 stop | HYPE | DOWN | 0.65 | open |  |
| 11-02 12:21 | +5 | HYPE | DOWN | 0.64 | open |  |
| 11-02 12:21 | +10 stop | DOGE | UP | 0.64 | 0.34 | -3.33 |
| 11-02 12:21 | +15 | DOGE | UP | 0.64 | open |  |
| 11-02 12:20 | +10 stop | XRP | UP | 0.57 | open |  |
| 11-02 12:20 | +10 | XRP | UP | 0.57 | open |  |
| 11-02 12:20 | +5 | XRP | UP | 0.56 | open |  |
| 11-02 12:20 | +5 | ETH | DOWN | 0.71 | 0.78 | 0.42 |
| 11-02 12:20 | +10 stop | ZEC | DOWN | 0.61 | open |  |
| 11-02 12:20 | +5 | HYPE | UP | 0.49 | 0.64 | 1.15 |
| 11-02 12:20 | +10 stop | SOL | UP | 0.51 | 0.32 | -2.24 |
| 11-02 12:20 | +10 | SOL | UP | 0.51 | open |  |
| 11-02 12:20 | +5 | SOL | UP | 0.51 | 0.56 | 0.14 |
| 11-02 12:19 | +5 | ETH | UP | 0.50 | 0.57 | 0.34 |
| 11-02 12:19 | +10 stop | ETH | UP | 0.52 | 0.36 | -1.95 |
| 11-02 12:19 | +10 stop | DOGE | UP | 0.69 | 0.51 | -2.13 |
| 11-02 12:19 | +10 | DOGE | UP | 0.69 | open |  |
| 11-02 12:19 | +5 | DOGE | UP | 0.69 | open |  |
| 11-02 12:19 | +10 stop | BTC | UP | 0.66 | 0.49 | -2.04 |
| 11-02 12:19 | +5 | HYPE | UP | 0.61 | 0.67 | 0.27 |
| 11-02 12:18 | +5 | DOGE | UP | 0.57 | 0.64 | 0.35 |
| 11-02 12:17 | +10 stop | ETH | DOWN | 0.62 | 0.46 | -1.95 |
| 11-02 12:17 | +10 stop | ZEC | DOWN | 0.60 | 0.44 | -1.95 |
| 11-02 12:17 | +5 | DOGE | UP | 0.53 | 0.58 | 0.14 |
| 11-02 12:16 | +10 stop | DOGE | UP | 0.54 | 0.64 | 0.65 |
| 11-02 12:16 | +20 | DOGE | UP | 0.54 | open |  |
| 11-02 12:16 | +15 | DOGE | UP | 0.54 | 0.73 | 1.58 |
| 11-02 12:16 | +10 | DOGE | UP | 0.54 | 0.64 | 0.65 |
| 11-02 12:16 | +5 | DOGE | UP | 0.54 | 0.61 | 0.35 |
| 11-02 12:16 | +10 stop | NEAR | UP | 0.67 | 0.49 | -2.14 |
| 11-02 12:16 | +20 | NEAR | UP | 0.67 | open |  |
| 11-02 12:16 | +15 | NEAR | UP | 0.67 | open |  |
| 11-02 12:16 | +10 | NEAR | UP | 0.67 | open |  |
| 11-02 12:16 | +5 | NEAR | UP | 0.67 | open |  |
| 11-02 12:16 | +10 stop | BTC | UP | 0.67 | 0.49 | -2.14 |
| 11-02 12:16 | +20 | BTC | UP | 0.67 | open |  |
| 11-02 12:16 | +15 | BTC | UP | 0.67 | open |  |
| 11-02 12:16 | +10 | BTC | UP | 0.67 | open |  |

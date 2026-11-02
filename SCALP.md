# Range-Scalp Bot

*Updated Mon Nov 02 23:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45299 | 39442 | 5857 (67) | 4 | $-13103.93 | -4.6% |
| **+10¢** | 33810 | 27024 | 6786 (89) | 5 | $-11974.40 | -5.6% |
| **+15¢** | 28280 | 20977 | 7303 (116) | 5 | $-11033.58 | -6.2% |
| **+20¢** | 25117 | 17469 | 7648 (151) | 5 | $-9790.29 | -6.2% |
| **+10¢ (15¢ stop)** | 55259 | 55172 | 87 (51) | 4 | $-20868.74 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 23:33 | +10 stop | DOGE | UP | 0.60 | open |  |
| 11-02 23:33 | +10 stop | SOL | UP | 0.62 | 0.72 | 0.68 |
| 11-02 23:33 | +10 stop | BTC | UP | 0.71 | open |  |
| 11-02 23:33 | +20 | BTC | UP | 0.71 | open |  |
| 11-02 23:33 | +15 | BTC | UP | 0.71 | open |  |
| 11-02 23:33 | +10 | BTC | UP | 0.70 | open |  |
| 11-02 23:33 | +5 | BTC | UP | 0.70 | 0.76 | 0.32 |
| 11-02 23:33 | +10 stop | ZEC | UP | 0.58 | open |  |
| 11-02 23:31 | +10 stop | SOL | DOWN | 0.57 | 0.35 | -2.54 |
| 11-02 23:31 | +20 | SOL | DOWN | 0.57 | open |  |
| 11-02 23:31 | +15 | SOL | DOWN | 0.57 | open |  |
| 11-02 23:31 | +10 | SOL | DOWN | 0.57 | open |  |
| 11-02 23:31 | +5 | SOL | DOWN | 0.57 | open |  |
| 11-02 23:31 | +10 stop | ZEC | DOWN | 0.62 | 0.44 | -2.15 |
| 11-02 23:31 | +20 | ZEC | DOWN | 0.62 | open |  |
| 11-02 23:31 | +15 | ZEC | DOWN | 0.63 | open |  |
| 11-02 23:31 | +10 | ZEC | DOWN | 0.63 | open |  |
| 11-02 23:31 | +5 | ZEC | DOWN | 0.63 | open |  |
| 11-02 23:31 | +10 stop | NEAR | DOWN | 0.62 | open |  |
| 11-02 23:31 | +20 | NEAR | DOWN | 0.62 | open |  |
| 11-02 23:31 | +15 | NEAR | DOWN | 0.62 | open |  |
| 11-02 23:31 | +10 | NEAR | DOWN | 0.62 | open |  |
| 11-02 23:31 | +5 | NEAR | DOWN | 0.62 | open |  |
| 11-02 23:31 | +10 stop | DOGE | DOWN | 0.63 | 0.37 | -2.94 |
| 11-02 23:31 | +20 | DOGE | DOWN | 0.63 | open |  |
| 11-02 23:31 | +15 | DOGE | DOWN | 0.63 | open |  |
| 11-02 23:31 | +10 | DOGE | DOWN | 0.63 | open |  |
| 11-02 23:31 | +5 | DOGE | DOWN | 0.63 | open |  |
| 11-02 23:30 | +10 stop | ETH | UP | 0.58 | 0.43 | -1.86 |
| 11-02 23:30 | +20 | ETH | UP | 0.59 | 0.82 | 2.02 |
| 11-02 23:30 | +15 | ETH | UP | 0.60 | 0.75 | 1.19 |
| 11-02 23:30 | +10 | ETH | UP | 0.60 | 0.72 | 0.88 |
| 11-02 23:30 | +5 | ETH | UP | 0.60 | 0.72 | 0.88 |
| 11-02 23:30 | +10 stop | XRP | UP | 0.60 | 0.77 | 1.40 |
| 11-02 23:30 | +20 | XRP | UP | 0.60 | 0.80 | 1.71 |
| 11-02 23:30 | +15 | XRP | UP | 0.60 | 0.77 | 1.40 |
| 11-02 23:30 | +10 | XRP | UP | 0.60 | 0.77 | 1.40 |
| 11-02 23:30 | +5 | XRP | UP | 0.60 | 0.67 | 0.37 |
| 11-02 23:24 | +10 stop | BTC | UP | 0.65 | 0.43 | -2.54 |
| 11-02 23:24 | +10 | BTC | UP | 0.71 | no | -7.25 |

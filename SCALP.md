# Range-Scalp Bot

*Updated Mon Nov 02 04:47 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44402 | 38660 | 5742 (65) | 7 | $-12882.76 | -4.6% |
| **+10¢** | 33144 | 26505 | 6639 (86) | 7 | $-11663.62 | -5.6% |
| **+15¢** | 27748 | 20603 | 7145 (113) | 7 | $-10671.21 | -6.1% |
| **+20¢** | 24660 | 17183 | 7477 (147) | 7 | $-9367.67 | -6.1% |
| **+10¢ (15¢ stop)** | 54191 | 54105 | 86 (51) | 7 | $-20588.46 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 04:46 | +10 stop | SOL | UP | 0.69 | open |  |
| 11-02 04:46 | +20 | SOL | UP | 0.69 | open |  |
| 11-02 04:46 | +15 | SOL | UP | 0.69 | open |  |
| 11-02 04:46 | +10 | SOL | UP | 0.69 | open |  |
| 11-02 04:46 | +5 | SOL | UP | 0.69 | open |  |
| 11-02 04:46 | +10 stop | DOGE | UP | 0.65 | open |  |
| 11-02 04:46 | +20 | DOGE | UP | 0.65 | open |  |
| 11-02 04:46 | +15 | DOGE | UP | 0.65 | open |  |
| 11-02 04:46 | +10 | DOGE | UP | 0.65 | open |  |
| 11-02 04:46 | +5 | DOGE | UP | 0.65 | open |  |
| 11-02 04:46 | +10 stop | XRP | DOWN | 0.57 | open |  |
| 11-02 04:46 | +20 | XRP | DOWN | 0.57 | open |  |
| 11-02 04:46 | +15 | XRP | DOWN | 0.57 | open |  |
| 11-02 04:46 | +10 | XRP | DOWN | 0.57 | open |  |
| 11-02 04:46 | +5 | XRP | DOWN | 0.57 | open |  |
| 11-02 04:46 | +10 stop | BTC | UP | 0.57 | open |  |
| 11-02 04:46 | +20 | BTC | UP | 0.57 | open |  |
| 11-02 04:46 | +15 | BTC | UP | 0.57 | open |  |
| 11-02 04:46 | +10 | BTC | UP | 0.56 | open |  |
| 11-02 04:46 | +5 | BTC | UP | 0.56 | open |  |
| 11-02 04:46 | +10 stop | ZEC | UP | 0.65 | open |  |
| 11-02 04:46 | +20 | ZEC | UP | 0.65 | open |  |
| 11-02 04:46 | +15 | ZEC | UP | 0.65 | open |  |
| 11-02 04:46 | +10 | ZEC | UP | 0.65 | open |  |
| 11-02 04:46 | +5 | ZEC | UP | 0.65 | open |  |
| 11-02 04:46 | +10 stop | HYPE | UP | 0.59 | open |  |
| 11-02 04:46 | +20 | HYPE | UP | 0.59 | open |  |
| 11-02 04:46 | +15 | HYPE | UP | 0.60 | open |  |
| 11-02 04:46 | +10 | HYPE | UP | 0.60 | open |  |
| 11-02 04:46 | +5 | HYPE | UP | 0.60 | open |  |
| 11-02 04:45 | +10 stop | ETH | DOWN | 0.55 | open |  |
| 11-02 04:45 | +20 | ETH | DOWN | 0.55 | open |  |
| 11-02 04:45 | +15 | ETH | DOWN | 0.55 | open |  |
| 11-02 04:45 | +10 | ETH | DOWN | 0.55 | open |  |
| 11-02 04:45 | +5 | ETH | DOWN | 0.55 | open |  |
| 11-02 04:34 | +10 stop | ZEC | DOWN | 0.70 | 0.83 | 1.05 |
| 11-02 04:33 | +10 stop | XRP | DOWN | 0.69 | 0.79 | 0.73 |
| 11-02 04:32 | +5 | SOL | DOWN | 0.68 | 0.74 | 0.30 |
| 11-02 04:32 | +10 stop | NEAR | DOWN | 0.67 | 0.79 | 0.92 |
| 11-02 04:32 | +10 stop | BTC | DOWN | 0.68 | 0.79 | 0.82 |

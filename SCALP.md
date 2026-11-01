# Range-Scalp Bot

*Updated Sun Nov 01 18:52 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43816 | 38175 | 5641 (65) | 4 | $-12524.77 | -4.5% |
| **+10¢** | 32685 | 26169 | 6516 (86) | 7 | $-11260.48 | -5.5% |
| **+15¢** | 27356 | 20340 | 7016 (113) | 7 | $-10283.77 | -6.0% |
| **+20¢** | 24296 | 16947 | 7349 (147) | 7 | $-9071.88 | -5.9% |
| **+10¢ (15¢ stop)** | 53443 | 53357 | 86 (51) | 0 | $-20201.87 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 18:49 | +10 stop | SOL | DOWN | 0.57 | 0.72 | 1.17 |
| 11-01 18:48 | +10 stop | BNB | DOWN | 0.62 | 0.90 | 2.51 |
| 11-01 18:48 | +10 stop | ZEC | DOWN | 0.68 | 0.79 | 0.82 |
| 11-01 18:48 | +5 | ZEC | DOWN | 0.68 | 0.75 | 0.40 |
| 11-01 18:48 | +10 stop | BTC | DOWN | 0.62 | 0.76 | 1.10 |
| 11-01 18:47 | +5 | XRP | DOWN | 0.66 | 0.79 | 1.02 |
| 11-01 18:47 | +5 | ZEC | DOWN | 0.64 | 0.73 | 0.59 |
| 11-01 18:47 | +10 stop | HYPE | DOWN | 0.70 | 0.83 | 1.05 |
| 11-01 18:47 | +20 | HYPE | DOWN | 0.70 | 0.92 | 2.00 |
| 11-01 18:47 | +15 | HYPE | DOWN | 0.70 | 0.85 | 1.26 |
| 11-01 18:47 | +10 | HYPE | DOWN | 0.70 | 0.83 | 1.05 |
| 11-01 18:47 | +5 | HYPE | DOWN | 0.70 | 0.76 | 0.32 |
| 11-01 18:47 | +10 stop | ETH | UP | 0.68 | 0.45 | -2.64 |
| 11-01 18:47 | +20 | ETH | UP | 0.68 | open |  |
| 11-01 18:47 | +15 | ETH | UP | 0.68 | open |  |
| 11-01 18:47 | +10 | ETH | UP | 0.68 | open |  |
| 11-01 18:47 | +5 | ETH | UP | 0.68 | open |  |
| 11-01 18:47 | +10 stop | SOL | UP | 0.59 | 0.40 | -2.24 |
| 11-01 18:47 | +20 | SOL | UP | 0.59 | open |  |
| 11-01 18:47 | +15 | SOL | UP | 0.59 | open |  |
| 11-01 18:47 | +10 | SOL | UP | 0.59 | open |  |
| 11-01 18:47 | +5 | SOL | UP | 0.59 | open |  |
| 11-01 18:47 | +5 | NEAR | DOWN | 0.51 | 0.56 | 0.14 |
| 11-01 18:46 | +10 stop | DOGE | DOWN | 0.64 | 0.75 | 0.79 |
| 11-01 18:46 | +20 | DOGE | DOWN | 0.64 | 0.84 | 1.73 |
| 11-01 18:46 | +15 | DOGE | DOWN | 0.64 | 0.84 | 1.73 |
| 11-01 18:46 | +10 | DOGE | DOWN | 0.64 | 0.75 | 0.79 |
| 11-01 18:46 | +5 | DOGE | DOWN | 0.64 | 0.71 | 0.38 |
| 11-01 18:46 | +10 stop | BNB | UP | 0.57 | 0.40 | -2.05 |
| 11-01 18:46 | +20 | BNB | UP | 0.57 | open |  |
| 11-01 18:46 | +15 | BNB | UP | 0.57 | open |  |
| 11-01 18:46 | +10 | BNB | UP | 0.57 | open |  |
| 11-01 18:46 | +5 | BNB | UP | 0.57 | open |  |
| 11-01 18:46 | +10 stop | ZEC | UP | 0.48 | 0.31 | -2.03 |
| 11-01 18:46 | +20 | ZEC | UP | 0.48 | open |  |
| 11-01 18:46 | +15 | ZEC | UP | 0.48 | open |  |
| 11-01 18:46 | +10 | ZEC | UP | 0.48 | open |  |
| 11-01 18:46 | +5 | ZEC | UP | 0.48 | 0.56 | 0.44 |
| 11-01 18:46 | +10 stop | BTC | UP | 0.62 | 0.39 | -2.64 |
| 11-01 18:46 | +20 | BTC | UP | 0.63 | open |  |

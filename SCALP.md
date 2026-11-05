# Range-Scalp Bot

*Updated Thu Nov 05 00:17 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47718 | 41546 | 6172 (73) | 4 | $-13793.49 | -4.6% |
| **+10¢** | 35662 | 28502 | 7160 (98) | 5 | $-12607.49 | -5.6% |
| **+15¢** | 29879 | 22169 | 7710 (126) | 6 | $-11544.66 | -6.2% |
| **+20¢** | 26553 | 18478 | 8075 (166) | 6 | $-10179.82 | -6.1% |
| **+10¢ (15¢ stop)** | 58178 | 58085 | 93 (56) | 5 | $-21618.33 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 00:16 | +10 stop | ZEC | DOWN | 0.50 | 0.64 | 1.05 |
| 11-05 00:16 | +20 | ZEC | DOWN | 0.53 | open |  |
| 11-05 00:16 | +15 | ZEC | DOWN | 0.53 | open |  |
| 11-05 00:16 | +10 | ZEC | DOWN | 0.54 | 0.64 | 0.65 |
| 11-05 00:16 | +5 | ZEC | DOWN | 0.54 | 0.64 | 0.65 |
| 11-05 00:16 | +10 stop | DOGE | UP | 0.68 | open |  |
| 11-05 00:16 | +20 | DOGE | UP | 0.68 | open |  |
| 11-05 00:16 | +15 | DOGE | UP | 0.68 | open |  |
| 11-05 00:16 | +10 | DOGE | UP | 0.68 | open |  |
| 11-05 00:16 | +5 | DOGE | UP | 0.68 | open |  |
| 11-05 00:16 | +10 stop | SOL | UP | 0.66 | open |  |
| 11-05 00:16 | +20 | SOL | UP | 0.67 | open |  |
| 11-05 00:16 | +15 | SOL | UP | 0.67 | open |  |
| 11-05 00:16 | +10 | SOL | UP | 0.67 | open |  |
| 11-05 00:16 | +5 | SOL | UP | 0.67 | open |  |
| 11-05 00:16 | +10 stop | XRP | DOWN | 0.59 | open |  |
| 11-05 00:16 | +20 | XRP | DOWN | 0.59 | open |  |
| 11-05 00:16 | +15 | XRP | DOWN | 0.59 | open |  |
| 11-05 00:16 | +10 | XRP | DOWN | 0.59 | open |  |
| 11-05 00:16 | +5 | XRP | DOWN | 0.59 | open |  |
| 11-05 00:16 | +5 | NEAR | UP | 0.58 | 0.63 | 0.15 |
| 11-05 00:15 | +10 stop | NEAR | UP | 0.57 | open |  |
| 11-05 00:15 | +20 | NEAR | UP | 0.57 | open |  |
| 11-05 00:15 | +15 | NEAR | UP | 0.57 | open |  |
| 11-05 00:15 | +10 | NEAR | UP | 0.57 | open |  |
| 11-05 00:15 | +5 | NEAR | UP | 0.57 | 0.63 | 0.25 |
| 11-05 00:15 | +10 stop | ETH | DOWN | 0.50 | open |  |
| 11-05 00:15 | +20 | ETH | DOWN | 0.50 | open |  |
| 11-05 00:15 | +15 | ETH | DOWN | 0.51 | open |  |
| 11-05 00:15 | +10 | ETH | DOWN | 0.51 | open |  |
| 11-05 00:15 | +5 | ETH | DOWN | 0.51 | open |  |
| 11-05 00:12 | +10 stop | DOGE | UP | 0.65 | 0.75 | 0.70 |
| 11-05 00:12 | +10 | DOGE | UP | 0.65 | 0.75 | 0.70 |
| 11-05 00:12 | +5 | DOGE | UP | 0.65 | 0.75 | 0.70 |
| 11-05 00:12 | +5 | SOL | UP | 0.62 | 0.68 | 0.27 |
| 11-05 00:11 | +10 stop | ETH | UP | 0.69 | 0.79 | 0.73 |
| 11-05 00:11 | +10 stop | SOL | UP | 0.59 | 0.78 | 1.60 |
| 11-05 00:11 | +15 | SOL | UP | 0.59 | 0.78 | 1.60 |
| 11-05 00:11 | +10 | SOL | UP | 0.60 | 0.78 | 1.50 |
| 11-05 00:11 | +5 | SOL | UP | 0.60 | 0.65 | 0.17 |

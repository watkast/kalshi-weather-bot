# Range-Scalp Bot

*Updated Thu Nov 12 06:17 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56752 | 49470 | 7282 (98) | 7 | $-15665.26 | -4.4% |
| **+10¢** | 42414 | 33921 | 8493 (128) | 7 | $-14599.47 | -5.5% |
| **+15¢** | 35559 | 26416 | 9143 (162) | 7 | $-13240.10 | -5.9% |
| **+20¢** | 31673 | 22079 | 9594 (212) | 7 | $-11636.38 | -5.9% |
| **+10¢ (15¢ stop)** | 69206 | 69083 | 123 (73) | 7 | $-25615.37 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 06:16 | +10 stop | HYPE | UP | 0.52 | open |  |
| 11-12 06:16 | +10 stop | BNB | UP | 0.60 | open |  |
| 11-12 06:16 | +20 | BNB | UP | 0.60 | open |  |
| 11-12 06:16 | +15 | BNB | UP | 0.60 | open |  |
| 11-12 06:16 | +10 | BNB | UP | 0.60 | open |  |
| 11-12 06:16 | +5 | BNB | UP | 0.60 | open |  |
| 11-12 06:16 | +10 stop | NEAR | UP | 0.64 | open |  |
| 11-12 06:15 | +10 stop | XRP | DOWN | 0.53 | open |  |
| 11-12 06:15 | +20 | XRP | DOWN | 0.53 | open |  |
| 11-12 06:15 | +15 | XRP | DOWN | 0.53 | open |  |
| 11-12 06:15 | +10 | XRP | DOWN | 0.53 | open |  |
| 11-12 06:15 | +5 | XRP | DOWN | 0.53 | open |  |
| 11-12 06:15 | +10 stop | BTC | DOWN | 0.55 | open |  |
| 11-12 06:15 | +20 | BTC | DOWN | 0.55 | open |  |
| 11-12 06:15 | +15 | BTC | DOWN | 0.56 | open |  |
| 11-12 06:15 | +10 | BTC | DOWN | 0.56 | open |  |
| 11-12 06:15 | +5 | BTC | DOWN | 0.58 | open |  |
| 11-12 06:15 | +10 stop | HYPE | DOWN | 0.60 | 0.45 | -1.85 |
| 11-12 06:15 | +20 | HYPE | DOWN | 0.61 | open |  |
| 11-12 06:15 | +15 | HYPE | DOWN | 0.60 | open |  |
| 11-12 06:15 | +10 | HYPE | DOWN | 0.60 | open |  |
| 11-12 06:15 | +5 | HYPE | DOWN | 0.61 | open |  |
| 11-12 06:15 | +10 stop | NEAR | DOWN | 0.59 | 0.42 | -2.05 |
| 11-12 06:15 | +20 | NEAR | DOWN | 0.59 | open |  |
| 11-12 06:15 | +15 | NEAR | DOWN | 0.59 | open |  |
| 11-12 06:15 | +10 | NEAR | DOWN | 0.59 | open |  |
| 11-12 06:15 | +5 | NEAR | DOWN | 0.59 | open |  |
| 11-12 06:15 | +10 stop | DOGE | DOWN | 0.58 | open |  |
| 11-12 06:15 | +20 | DOGE | DOWN | 0.58 | open |  |
| 11-12 06:15 | +15 | DOGE | DOWN | 0.58 | open |  |
| 11-12 06:15 | +10 | DOGE | DOWN | 0.58 | open |  |
| 11-12 06:15 | +5 | DOGE | DOWN | 0.58 | open |  |
| 11-12 06:15 | +10 stop | ETH | DOWN | 0.58 | open |  |
| 11-12 06:15 | +20 | ETH | DOWN | 0.58 | open |  |
| 11-12 06:15 | +15 | ETH | DOWN | 0.58 | open |  |
| 11-12 06:15 | +10 | ETH | DOWN | 0.57 | open |  |
| 11-12 06:15 | +5 | ETH | DOWN | 0.57 | open |  |
| 11-12 06:10 | +10 stop | HYPE | UP | 0.71 | 0.83 | 0.95 |
| 11-12 06:10 | +10 stop | NEAR | UP | 0.50 | 0.70 | 1.67 |
| 11-12 06:10 | +10 | NEAR | UP | 0.50 | 0.70 | 1.67 |

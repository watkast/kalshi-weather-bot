# Range-Scalp Bot

*Updated Wed Nov 04 22:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47625 | 41467 | 6158 (73) | 2 | $-13746.89 | -4.6% |
| **+10¢** | 35588 | 28446 | 7142 (98) | 2 | $-12554.87 | -5.6% |
| **+15¢** | 29818 | 22126 | 7692 (126) | 2 | $-11499.89 | -6.1% |
| **+20¢** | 26498 | 18441 | 8057 (166) | 2 | $-10145.76 | -6.1% |
| **+10¢ (15¢ stop)** | 58059 | 57966 | 93 (56) | 0 | $-21594.54 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 22:37 | +10 stop | HYPE | UP | 0.62 | 0.76 | 1.10 |
| 11-04 22:35 | +10 stop | HYPE | UP | 0.69 | 0.52 | -2.03 |
| 11-04 22:34 | +5 | BTC | UP | 0.65 | 0.71 | 0.29 |
| 11-04 22:32 | +10 stop | ETH | UP | 0.68 | 0.91 | 2.06 |
| 11-04 22:32 | +20 | ETH | UP | 0.68 | 0.91 | 2.06 |
| 11-04 22:32 | +15 | ETH | UP | 0.68 | 0.91 | 2.06 |
| 11-04 22:32 | +10 | ETH | UP | 0.68 | 0.91 | 2.06 |
| 11-04 22:32 | +5 | ETH | UP | 0.68 | 0.76 | 0.51 |
| 11-04 22:32 | +10 stop | XRP | UP | 0.71 | 0.86 | 1.26 |
| 11-04 22:32 | +20 | XRP | UP | 0.71 | 0.93 | 1.95 |
| 11-04 22:32 | +15 | XRP | UP | 0.71 | 0.86 | 1.26 |
| 11-04 22:32 | +10 | XRP | UP | 0.71 | 0.86 | 1.26 |
| 11-04 22:32 | +5 | XRP | UP | 0.71 | 0.76 | 0.22 |
| 11-04 22:32 | +10 stop | BTC | UP | 0.54 | 0.64 | 0.65 |
| 11-04 22:32 | +20 | BTC | UP | 0.54 | 0.77 | 1.99 |
| 11-04 22:32 | +15 | BTC | UP | 0.55 | 0.71 | 1.27 |
| 11-04 22:32 | +10 | BTC | UP | 0.55 | 0.71 | 1.27 |
| 11-04 22:32 | +5 | BTC | UP | 0.55 | 0.60 | 0.15 |
| 11-04 22:31 | +10 stop | SOL | UP | 0.67 | 0.78 | 0.81 |
| 11-04 22:31 | +10 stop | HYPE | DOWN | 0.58 | 0.33 | -2.84 |
| 11-04 22:31 | +20 | HYPE | DOWN | 0.58 | open |  |
| 11-04 22:31 | +15 | HYPE | DOWN | 0.58 | open |  |
| 11-04 22:31 | +10 | HYPE | DOWN | 0.58 | open |  |
| 11-04 22:31 | +5 | HYPE | DOWN | 0.58 | open |  |
| 11-04 22:31 | +10 stop | BNB | UP | 0.65 | 0.87 | 1.96 |
| 11-04 22:31 | +20 | BNB | UP | 0.65 | 0.87 | 1.96 |
| 11-04 22:31 | +15 | BNB | UP | 0.65 | 0.87 | 1.96 |
| 11-04 22:31 | +10 | BNB | UP | 0.65 | 0.87 | 1.96 |
| 11-04 22:31 | +5 | BNB | UP | 0.65 | 0.70 | 0.19 |
| 11-04 22:31 | +10 stop | ZEC | UP | 0.70 | 0.83 | 1.05 |
| 11-04 22:31 | +20 | ZEC | UP | 0.70 | 0.93 | 2.13 |
| 11-04 22:31 | +15 | ZEC | UP | 0.70 | 0.93 | 2.13 |
| 11-04 22:31 | +10 | ZEC | UP | 0.70 | 0.83 | 1.05 |
| 11-04 22:31 | +5 | ZEC | UP | 0.70 | 0.78 | 0.52 |
| 11-04 22:30 | +10 stop | SOL | DOWN | 0.60 | 0.44 | -1.95 |
| 11-04 22:30 | +20 | SOL | DOWN | 0.60 | open |  |
| 11-04 22:30 | +15 | SOL | DOWN | 0.60 | open |  |
| 11-04 22:30 | +10 | SOL | DOWN | 0.60 | open |  |
| 11-04 22:30 | +5 | SOL | DOWN | 0.60 | open |  |
| 11-04 22:28 | +10 stop | ZEC | DOWN | 0.67 | 0.52 | -1.84 |

# Range-Scalp Bot

*Updated Wed Nov 18 13:51 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63990 | 55808 | 8182 (124) | 6 | $-17460.85 | -4.3% |
| **+10¢** | 47803 | 38229 | 9574 (165) | 6 | $-16353.40 | -5.4% |
| **+15¢** | 40082 | 29761 | 10321 (210) | 6 | $-14808.39 | -5.9% |
| **+20¢** | 35695 | 24860 | 10835 (265) | 7 | $-13115.22 | -5.9% |
| **+10¢ (15¢ stop)** | 77837 | 77673 | 164 (98) | 6 | $-28571.63 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 13:51 | +5 | DOGE | UP | 0.65 | open |  |
| 11-18 13:51 | +10 stop | SOL | UP | 0.67 | open |  |
| 11-18 13:51 | +10 | SOL | UP | 0.67 | open |  |
| 11-18 13:51 | +5 | SOL | UP | 0.67 | open |  |
| 11-18 13:49 | +10 stop | HYPE | DOWN | 0.67 | 0.78 | 0.81 |
| 11-18 13:49 | +10 | HYPE | DOWN | 0.67 | 0.78 | 0.81 |
| 11-18 13:49 | +5 | SOL | UP | 0.58 | 0.67 | 0.56 |
| 11-18 13:49 | +10 stop | BTC | UP | 0.61 | open |  |
| 11-18 13:49 | +10 stop | ETH | UP | 0.60 | open |  |
| 11-18 13:48 | +10 stop | SOL | UP | 0.54 | 0.67 | 0.96 |
| 11-18 13:48 | +20 | SOL | UP | 0.54 | open |  |
| 11-18 13:48 | +15 | SOL | UP | 0.54 | open |  |
| 11-18 13:48 | +10 | SOL | UP | 0.54 | 0.67 | 0.96 |
| 11-18 13:48 | +5 | SOL | UP | 0.54 | 0.60 | 0.25 |
| 11-18 13:48 | +5 | HYPE | DOWN | 0.63 | 0.73 | 0.69 |
| 11-18 13:48 | +5 | ETH | DOWN | 0.56 | open |  |
| 11-18 13:47 | +10 stop | DOGE | UP | 0.58 | open |  |
| 11-18 13:47 | +20 | DOGE | UP | 0.58 | open |  |
| 11-18 13:47 | +15 | DOGE | UP | 0.58 | open |  |
| 11-18 13:47 | +10 | DOGE | UP | 0.58 | open |  |
| 11-18 13:47 | +5 | DOGE | UP | 0.58 | 0.65 | 0.38 |
| 11-18 13:47 | +10 stop | XRP | UP | 0.59 | 0.71 | 0.88 |
| 11-18 13:47 | +20 | XRP | UP | 0.59 | open |  |
| 11-18 13:47 | +15 | XRP | UP | 0.59 | 0.76 | 1.40 |
| 11-18 13:47 | +10 | XRP | UP | 0.59 | 0.71 | 0.88 |
| 11-18 13:47 | +5 | XRP | UP | 0.59 | 0.64 | 0.16 |
| 11-18 13:47 | +10 stop | ZEC | UP | 0.59 | open |  |
| 11-18 13:47 | +20 | ZEC | UP | 0.59 | open |  |
| 11-18 13:47 | +15 | ZEC | UP | 0.59 | open |  |
| 11-18 13:47 | +10 | ZEC | UP | 0.59 | open |  |
| 11-18 13:47 | +5 | ZEC | UP | 0.59 | open |  |
| 11-18 13:47 | +5 | ETH | DOWN | 0.53 | 0.59 | 0.21 |
| 11-18 13:47 | +10 stop | BTC | DOWN | 0.52 | 0.37 | -1.85 |
| 11-18 13:47 | +20 | BTC | DOWN | 0.53 | open |  |
| 11-18 13:47 | +15 | BTC | DOWN | 0.53 | open |  |
| 11-18 13:47 | +10 | BTC | DOWN | 0.53 | open |  |
| 11-18 13:47 | +5 | BTC | DOWN | 0.53 | open |  |
| 11-18 13:47 | +10 stop | HYPE | DOWN | 0.52 | 0.65 | 0.96 |
| 11-18 13:47 | +20 | HYPE | DOWN | 0.52 | 0.73 | 1.78 |
| 11-18 13:47 | +15 | HYPE | DOWN | 0.52 | 0.67 | 1.16 |
